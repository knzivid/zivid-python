import zivid


def to_settings(internal_settings):
    def _to_acquisition(internal_acquisition):
        def _to_patterns(internal_patterns):
            def _to_sine(internal_sine):

                return zivid.Settings.Acquisition.Patterns.Sine(
                    bidirectional=internal_sine.bidirectional.value,
                )

            return zivid.Settings.Acquisition.Patterns(
                sine=_to_sine(internal_patterns.sine),
            )

        return zivid.Settings.Acquisition(
            patterns=_to_patterns(internal_acquisition.patterns),
            aperture=internal_acquisition.aperture.value,
            brightness=internal_acquisition.brightness.value,
            exposure_time=internal_acquisition.exposuretime.value,
            gain=internal_acquisition.gain.value,
        )

    def _to_processing(internal_processing):
        def _to_color(internal_color):
            def _to_balance(internal_balance):

                return zivid.Settings.Processing.Color.Balance(
                    blue=internal_balance.blue.value,
                    green=internal_balance.green.value,
                    red=internal_balance.red.value,
                )

            return zivid.Settings.Processing.Color(
                balance=_to_balance(internal_color.balance),
            )

        def _to_filters(internal_filters):
            def _to_experimental(internal_experimental):
                def _to_contrast_distortion(internal_contrast_distortion):
                    def _to_correction(internal_correction):

                        return zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Correction(
                            enabled=internal_correction.enabled.value,
                            strength=internal_correction.strength.value,
                        )

                    def _to_removal(internal_removal):

                        return zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Removal(
                            enabled=internal_removal.enabled.value,
                            threshold=internal_removal.threshold.value,
                        )

                    return zivid.Settings.Processing.Filters.Experimental.ContrastDistortion(
                        correction=_to_correction(
                            internal_contrast_distortion.correction
                        ),
                        removal=_to_removal(internal_contrast_distortion.removal),
                    )

                return zivid.Settings.Processing.Filters.Experimental(
                    contrast_distortion=_to_contrast_distortion(
                        internal_experimental.contrastdistortion
                    ),
                )

            def _to_noise(internal_noise):
                def _to_removal(internal_removal):

                    return zivid.Settings.Processing.Filters.Noise.Removal(
                        enabled=internal_removal.enabled.value,
                        threshold=internal_removal.threshold.value,
                    )

                return zivid.Settings.Processing.Filters.Noise(
                    removal=_to_removal(internal_noise.removal),
                )

            def _to_outlier(internal_outlier):
                def _to_removal(internal_removal):

                    return zivid.Settings.Processing.Filters.Outlier.Removal(
                        enabled=internal_removal.enabled.value,
                        threshold=internal_removal.threshold.value,
                    )

                return zivid.Settings.Processing.Filters.Outlier(
                    removal=_to_removal(internal_outlier.removal),
                )

            def _to_reflection(internal_reflection):
                def _to_removal(internal_removal):

                    return zivid.Settings.Processing.Filters.Reflection.Removal(
                        enabled=internal_removal.enabled.value,
                    )

                return zivid.Settings.Processing.Filters.Reflection(
                    removal=_to_removal(internal_reflection.removal),
                )

            def _to_smoothing(internal_smoothing):
                def _to_gaussian(internal_gaussian):

                    return zivid.Settings.Processing.Filters.Smoothing.Gaussian(
                        enabled=internal_gaussian.enabled.value,
                        sigma=internal_gaussian.sigma.value,
                    )

                return zivid.Settings.Processing.Filters.Smoothing(
                    gaussian=_to_gaussian(internal_smoothing.gaussian),
                )

            return zivid.Settings.Processing.Filters(
                experimental=_to_experimental(internal_filters.experimental),
                noise=_to_noise(internal_filters.noise),
                outlier=_to_outlier(internal_filters.outlier),
                reflection=_to_reflection(internal_filters.reflection),
                smoothing=_to_smoothing(internal_filters.smoothing),
            )

        return zivid.Settings.Processing(
            color=_to_color(internal_processing.color),
            filters=_to_filters(internal_processing.filters),
        )

    return zivid.Settings(
        processing=_to_processing(internal_settings.processing),
        acquisitions=[
            _to_acquisition(element) for element in internal_settings.acquisitions.value
        ],
    )


import _zivid


def to_internal_settings(settings):
    internal_settings = _zivid.Settings()

    def _to_internal_acquisition(acquisition):
        internal_acquisition = _zivid.Settings.Acquisition()

        def _to_internal_patterns(patterns):
            internal_patterns = _zivid.Settings.Acquisition.Patterns()

            def _to_internal_sine(sine):
                internal_sine = _zivid.Settings.Acquisition.Patterns.Sine()

                if sine.bidirectional is not None:

                    internal_sine.bidirectional = _zivid.Settings.Acquisition.Patterns.Sine.Bidirectional(
                        sine.bidirectional
                    )
                else:
                    internal_sine.bidirectional = (
                        _zivid.Settings.Acquisition.Patterns.Sine.Bidirectional()
                    )
                pass  # no children
                return internal_sine

            internal_patterns.sine = _to_internal_sine(patterns.sine)
            return internal_patterns

        if acquisition.aperture is not None:
            print(acquisition.aperture)
            print(type(acquisition.aperture))

            internal_acquisition.aperture = _zivid.Settings.Acquisition.Aperture(
                acquisition.aperture
            )
        else:
            internal_acquisition.aperture = _zivid.Settings.Acquisition.Aperture()
        if acquisition.brightness is not None:

            internal_acquisition.brightness = _zivid.Settings.Acquisition.Brightness(
                acquisition.brightness
            )
        else:
            internal_acquisition.brightness = _zivid.Settings.Acquisition.Brightness()
        if acquisition.exposure_time is not None:

            internal_acquisition.exposure_time = _zivid.Settings.Acquisition.ExposureTime(
                acquisition.exposure_time
            )
        else:
            internal_acquisition.exposure_time = (
                _zivid.Settings.Acquisition.ExposureTime()
            )
        if acquisition.gain is not None:

            internal_acquisition.gain = _zivid.Settings.Acquisition.Gain(
                acquisition.gain
            )
        else:
            internal_acquisition.gain = _zivid.Settings.Acquisition.Gain()

        internal_acquisition.patterns = _to_internal_patterns(acquisition.patterns)
        return internal_acquisition

    def _to_internal_processing(processing):
        internal_processing = _zivid.Settings.Processing()

        def _to_internal_color(color):
            internal_color = _zivid.Settings.Processing.Color()

            def _to_internal_balance(balance):
                internal_balance = _zivid.Settings.Processing.Color.Balance()

                if balance.blue is not None:

                    internal_balance.blue = _zivid.Settings.Processing.Color.Balance.Blue(
                        balance.blue
                    )
                else:
                    internal_balance.blue = (
                        _zivid.Settings.Processing.Color.Balance.Blue()
                    )
                if balance.green is not None:

                    internal_balance.green = _zivid.Settings.Processing.Color.Balance.Green(
                        balance.green
                    )
                else:
                    internal_balance.green = (
                        _zivid.Settings.Processing.Color.Balance.Green()
                    )
                if balance.red is not None:

                    internal_balance.red = _zivid.Settings.Processing.Color.Balance.Red(
                        balance.red
                    )
                else:
                    internal_balance.red = (
                        _zivid.Settings.Processing.Color.Balance.Red()
                    )
                pass  # no children
                return internal_balance

            internal_color.balance = _to_internal_balance(color.balance)
            return internal_color

        def _to_internal_filters(filters):
            internal_filters = _zivid.Settings.Processing.Filters()

            def _to_internal_experimental(experimental):
                internal_experimental = (
                    _zivid.Settings.Processing.Filters.Experimental()
                )

                def _to_internal_contrast_distortion(contrast_distortion):
                    internal_contrast_distortion = (
                        _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion()
                    )

                    def _to_internal_correction(correction):
                        internal_correction = (
                            _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Correction()
                        )

                        if correction.enabled is not None:

                            internal_correction.enabled = _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Correction.Enabled(
                                correction.enabled
                            )
                        else:
                            internal_correction.enabled = (
                                _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Correction.Enabled()
                            )
                        if correction.strength is not None:

                            internal_correction.strength = _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Correction.Strength(
                                correction.strength
                            )
                        else:
                            internal_correction.strength = (
                                _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Correction.Strength()
                            )
                        pass  # no children
                        return internal_correction

                    def _to_internal_removal(removal):
                        internal_removal = (
                            _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Removal()
                        )

                        if removal.enabled is not None:

                            internal_removal.enabled = _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Removal.Enabled(
                                removal.enabled
                            )
                        else:
                            internal_removal.enabled = (
                                _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Removal.Enabled()
                            )
                        if removal.threshold is not None:

                            internal_removal.threshold = _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Removal.Threshold(
                                removal.threshold
                            )
                        else:
                            internal_removal.threshold = (
                                _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Removal.Threshold()
                            )
                        pass  # no children
                        return internal_removal

                    internal_contrast_distortion.correction = _to_internal_correction(
                        contrast_distortion.correction
                    )
                    internal_contrast_distortion.removal = _to_internal_removal(
                        contrast_distortion.removal
                    )
                    return internal_contrast_distortion

                internal_experimental.contrast_distortion = _to_internal_contrast_distortion(
                    experimental.contrast_distortion
                )
                return internal_experimental

            def _to_internal_noise(noise):
                internal_noise = _zivid.Settings.Processing.Filters.Noise()

                def _to_internal_removal(removal):
                    internal_removal = (
                        _zivid.Settings.Processing.Filters.Noise.Removal()
                    )

                    if removal.enabled is not None:

                        internal_removal.enabled = _zivid.Settings.Processing.Filters.Noise.Removal.Enabled(
                            removal.enabled
                        )
                    else:
                        internal_removal.enabled = (
                            _zivid.Settings.Processing.Filters.Noise.Removal.Enabled()
                        )
                    if removal.threshold is not None:

                        internal_removal.threshold = _zivid.Settings.Processing.Filters.Noise.Removal.Threshold(
                            removal.threshold
                        )
                    else:
                        internal_removal.threshold = (
                            _zivid.Settings.Processing.Filters.Noise.Removal.Threshold()
                        )
                    pass  # no children
                    return internal_removal

                internal_noise.removal = _to_internal_removal(noise.removal)
                return internal_noise

            def _to_internal_outlier(outlier):
                internal_outlier = _zivid.Settings.Processing.Filters.Outlier()

                def _to_internal_removal(removal):
                    internal_removal = (
                        _zivid.Settings.Processing.Filters.Outlier.Removal()
                    )

                    if removal.enabled is not None:

                        internal_removal.enabled = _zivid.Settings.Processing.Filters.Outlier.Removal.Enabled(
                            removal.enabled
                        )
                    else:
                        internal_removal.enabled = (
                            _zivid.Settings.Processing.Filters.Outlier.Removal.Enabled()
                        )
                    if removal.threshold is not None:

                        internal_removal.threshold = _zivid.Settings.Processing.Filters.Outlier.Removal.Threshold(
                            removal.threshold
                        )
                    else:
                        internal_removal.threshold = (
                            _zivid.Settings.Processing.Filters.Outlier.Removal.Threshold()
                        )
                    pass  # no children
                    return internal_removal

                internal_outlier.removal = _to_internal_removal(outlier.removal)
                return internal_outlier

            def _to_internal_reflection(reflection):
                internal_reflection = _zivid.Settings.Processing.Filters.Reflection()

                def _to_internal_removal(removal):
                    internal_removal = (
                        _zivid.Settings.Processing.Filters.Reflection.Removal()
                    )

                    if removal.enabled is not None:

                        internal_removal.enabled = _zivid.Settings.Processing.Filters.Reflection.Removal.Enabled(
                            removal.enabled
                        )
                    else:
                        internal_removal.enabled = (
                            _zivid.Settings.Processing.Filters.Reflection.Removal.Enabled()
                        )
                    pass  # no children
                    return internal_removal

                internal_reflection.removal = _to_internal_removal(reflection.removal)
                return internal_reflection

            def _to_internal_smoothing(smoothing):
                internal_smoothing = _zivid.Settings.Processing.Filters.Smoothing()

                def _to_internal_gaussian(gaussian):
                    internal_gaussian = (
                        _zivid.Settings.Processing.Filters.Smoothing.Gaussian()
                    )

                    if gaussian.enabled is not None:

                        internal_gaussian.enabled = _zivid.Settings.Processing.Filters.Smoothing.Gaussian.Enabled(
                            gaussian.enabled
                        )
                    else:
                        internal_gaussian.enabled = (
                            _zivid.Settings.Processing.Filters.Smoothing.Gaussian.Enabled()
                        )
                    if gaussian.sigma is not None:

                        internal_gaussian.sigma = _zivid.Settings.Processing.Filters.Smoothing.Gaussian.Sigma(
                            gaussian.sigma
                        )
                    else:
                        internal_gaussian.sigma = (
                            _zivid.Settings.Processing.Filters.Smoothing.Gaussian.Sigma()
                        )
                    pass  # no children
                    return internal_gaussian

                internal_smoothing.gaussian = _to_internal_gaussian(smoothing.gaussian)
                return internal_smoothing

            internal_filters.experimental = _to_internal_experimental(
                filters.experimental
            )
            internal_filters.noise = _to_internal_noise(filters.noise)
            internal_filters.outlier = _to_internal_outlier(filters.outlier)
            internal_filters.reflection = _to_internal_reflection(filters.reflection)
            internal_filters.smoothing = _to_internal_smoothing(filters.smoothing)
            return internal_filters

        internal_processing.color = _to_internal_color(processing.color)
        internal_processing.filters = _to_internal_filters(processing.filters)
        return internal_processing

    if settings.acquisitions is None:

        internal_settings.acquisitions = _zivid.Settings().Acquisitions()  # TODO
    else:
        temp = _zivid.Settings().Acquisitions()
        for acq in settings.acquisitions:
            temp.append(_to_internal_acquisition(acq))
        internal_settings.acquisitions = temp

    internal_settings.processing = _to_internal_processing(settings.processing)
    return internal_settings
