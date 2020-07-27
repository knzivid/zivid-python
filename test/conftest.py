import tempfile
import numbers
import os
import subprocess
from pathlib import Path

import pytest
import zivid

from scripts.sample_data import download_and_extract


@pytest.fixture(name="application")
def application_fixture():
    with zivid.Application() as app:
        yield app


@pytest.fixture(name="sample_data_file", scope="session")
def sample_data_file_fixture():
    with tempfile.TemporaryDirectory() as temp_dir:
        point_cloud_destination = Path(temp_dir) / "MiscObjects.zdf"
        file_camera_destination = Path(temp_dir) / "FileCameraZividOne.zfc"
        download_and_extract(
            file_camera_destination=file_camera_destination,
            point_cloud_destination=point_cloud_destination,
        )
        yield point_cloud_destination, file_camera_destination


@pytest.fixture(name="sample_point_cloud")
def sample_point_cloud_fixture(sample_data_file):
    yield sample_data_file[0]


@pytest.fixture(name="file_camera_file")
def file_camera_file_fixture(sample_data_file):
    yield sample_data_file[1]


@pytest.fixture(name="file_camera")
def file_camera_fixture(application, file_camera_file):
    with application.create_file_camera(file_camera_file) as file_cam:
        yield file_cam


@pytest.fixture(name="physical_camera")
def physical_camera_fixture(application):
    with application.connect_camera() as cam:
        yield cam


@pytest.fixture(name="frame")
def frame_fixture(application, sample_point_cloud):  # pylint: disable=unused-argument
    with zivid.Frame(sample_point_cloud) as frame:
        yield frame


@pytest.fixture(name="physical_camera_frame_2d")
def physical_camera_frame_2d_fixture(physical_camera):
    settings_2d = zivid.Settings2D()
    with physical_camera.capture_2d(settings_2d) as frame_2d:
        yield frame_2d


@pytest.fixture(name="physical_camera_image_2d")
def physical_camera_image_2d_fixture(physical_camera_frame_2d):
    with physical_camera_frame_2d.image() as image_2d:
        yield image_2d


@pytest.fixture(name="point_cloud")
def point_cloud_fixture(frame):
    with frame.point_cloud() as point_cloud:
        yield point_cloud


@pytest.fixture(name="three_frames")
def three_frames_fixture(
    application, sample_point_cloud  # pylint: disable=unused-argument
):
    frames = [zivid.Frame(sample_point_cloud)] * 3
    yield frames
    for fram in frames:
        fram.release()


@pytest.fixture(name="file_camera_info")
def file_camera_info_fixture(file_camera):
    yield file_camera.info


@pytest.fixture(name="frame_info")
def frame_info_fixture(frame):
    yield frame.info


@pytest.helpers.register
def set_attribute_tester(settings_instance, member, value, expected_data_type):
    if not hasattr(settings_instance, member):
        raise RuntimeError(
            "Settings instance {settings_instance} does not have the member: {member}".format(
                settings_instance=settings_instance, member=member
            )
        )
    setattr(settings_instance, member, value)
    assert getattr(settings_instance, member) == value
    assert isinstance(getattr(settings_instance, member), expected_data_type)

    class DummyClass:
        pass  # pylint: disable=too-few-public-methods

    with pytest.raises(TypeError):
        setattr(settings_instance, member, DummyClass())
    if expected_data_type in (int, float, numbers.Real):
        with pytest.raises(IndexError):
            setattr(settings_instance, member, 999999999999)
            setattr(settings_instance, member, -999999999999)
    elif expected_data_type == bool:
        pass
    else:
        with pytest.raises(TypeError):
            setattr(settings_instance, member, True)


@pytest.helpers.register
def equality_tester(settings_type, value_collection_1, value_collection_2):
    instance_1 = settings_type(*value_collection_1)
    instance_2 = settings_type(*value_collection_1)
    assert instance_1 == instance_2

    instance_3 = settings_type(*value_collection_2)
    assert instance_1 != instance_3
    assert instance_3 != instance_2


class Cd:
    def __init__(self, new_path):
        self.new_path = new_path
        self.saved_path = None

    def __enter__(self):
        self.saved_path = os.getcwd()
        os.chdir(str(self.new_path))

    def __exit__(self, etype, value, traceback):
        os.chdir(str(self.saved_path))


@pytest.helpers.register
def run_sample(name, working_directory=None):
    current_working_directory = Path(os.getcwd()).resolve()
    sample = (
        current_working_directory
        / ".."
        / ".."
        / "samples"
        / "sample_{name}.py".format(name=name)
    ).resolve()

    if working_directory is not None:
        with Cd(working_directory):
            subprocess.check_output(args=("python", str(sample),))
    else:
        subprocess.check_output(args=("python", str(sample),))
