"""Contains capture assistant functions and classes."""
import _zivid
import zivid._settings_converter as _settings_converter
from zivid._make_enum_wrapper import _make_enum_wrapper
from zivid._suggest_settings_converter import to_internal_suggest_settings_parameters


class SuggestSettingsParameters:
    class AmbientLightFrequency:
        hz50 = "hz50"  # class
        hz60 = "hz60"
        none = "none"

        _valid_values = {
            "hz50": _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.enum.hz50,
            "hz60": _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.enum.hz60,
            "none": _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.enum.none,
        }
        # hz50 = (
        #    _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.enum.hz50
        # )
        # hz60 = (
        #    _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.enum.hz60
        # )
        # none = (
        #    _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.enum.none
        # )
        @property
        def valid_values(cls):
            return [
                hz50,
                hz60,
                none,
            ]  # [to_ambient_light_frequency(value) for value in _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency().valid_values()]

        def _convert_to_internal_value(self, value):
            try:
                return self._valid_values[value]
            except Exception as ex:
                raise RuntimeError("failed again") from ex  # TODO

        def _is_valid_internal_value(self, value):
            if value in self._valid_values:
                return True
            return False
            # except Exception as ex:
            #     raise RuntimeError("failed again") from ex  # TODO

        @property
        def value(self):
            return self._value
            # print(self._valid_values.items())
            # for (
            #     key,
            #     internal_value,
            # ) in (
            #     self._valid_values.items()
            # ):
            #     print(f"Looking at value: {key}: {internal_value}")
            #     print(f"using value: {self._value}")
            #     if internal_value == self._value:
            #         return key
            # raise ValueError(f"Unsupported value: {self._value}")

        @value.setter
        def value(self, value):
            # if value in self.valid_values:
            if self._is_valid_internal_value(value):
                self._value = value
            else:
                raise ValueError(f"Unsupported value: {value}")

        # @property.setter
        # def hz50(self,value):
        #     if in dict("hz50": _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.enum.hz50):
        #        self._value = _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.enum.hz50
        #     else:
        #         raise ValueError(f"{value} is not in {self.valid_values()}")
        #         #raise sosdmksm

        def __init__(self, value=none):
            self._value = value

        def __eq__(self, other):
            if self._value == other._value:
                return True
            return False

        def __str__(self):
            return """AmbientLightFrequency: {value}""".format(value=self._value)

    def __init__(
        self,
        max_capture_time=_zivid.capture_assistant.SuggestSettingsParameters()
        .MaxCaptureTime()
        .value,
        ambient_light_frequency=AmbientLightFrequency(),
    ):

        if max_capture_time is not None:
            self._max_capture_time = _zivid.capture_assistant.SuggestSettingsParameters.MaxCaptureTime(
                max_capture_time
            )
        else:
            self._max_capture_time = (
                _zivid.capture_assistant.SuggestSettingsParameters.MaxCaptureTime()
            )
        self.ambient_light_frequency = ambient_light_frequency

    @property
    def max_capture_time(self):
        return self._max_capture_time.value

    @max_capture_time.setter
    def max_capture_time(self, value):
        self._max_capture_time = _zivid.capture_assistant.SuggestSettingsParameters.MaxCaptureTime(
            value
        )

    def __eq__(self, other):
        if (
            self._max_capture_time == other._max_capture_time
            and self.ambient_light_frequency == other.ambient_light_frequency
        ):
            return True
        return False

    def __str__(self):
        return """SuggestSettingsParameters:
    max_capture_time: {max_capture_time}
    ambient_light_frequency: {ambient_light_frequency}
    """.format(
            max_capture_time=self.max_capture_time,
            ambient_light_frequency=self.ambient_light_frequency,
        )


def suggest_settings(camera, suggest_settings_parameters):
    """Find settings for the current scene based on the suggest_settings_parameters.

    The suggested settings returned from this function should be passed into hdr.capture to perform the actual capture.

    Args:
        camera: an instance of zivid.Camera
        suggest_settings_parameters: an instance of zivid.capture_assistant.SuggestSettingsParameters which provides
                                     parameters (e.g., max capture time constraint) to the suggest_settings algorithm.

    Returns:
        Settings instance

    """
    internal_settings = _zivid.capture_assistant.suggest_settings(
        camera._Camera__impl,  # pylint: disable=protected-access
        to_internal_suggest_settings_parameters(suggest_settings_parameters),
    )
    return _settings_converter.to_settings(internal_settings)
