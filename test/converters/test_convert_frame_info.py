# pylint: disable=import-outside-toplevel


def test_to_internal_frame_info_to_frame_info_modified():
    import datetime
    from zivid import FrameInfo
    from zivid._frame_info_converter import to_frame_info, to_internal_frame_info

    modified_frame_info = FrameInfo(time_stamp="hello")

    converted_frame_info = to_frame_info(to_internal_frame_info(modified_frame_info))
    assert modified_frame_info == converted_frame_info
    assert isinstance(converted_frame_info, FrameInfo)
    assert isinstance(modified_frame_info, FrameInfo)


def test_to_internal_frame_info_to_frame_info_default():
    from zivid import FrameInfo
    from zivid._frame_info_converter import to_frame_info, to_internal_frame_info

    default_frame_info = FrameInfo()
    converted_frame_info = to_frame_info(to_internal_frame_info(default_frame_info))
    assert default_frame_info == converted_frame_info
    assert isinstance(converted_frame_info, FrameInfo)
    assert isinstance(default_frame_info, FrameInfo)


#
