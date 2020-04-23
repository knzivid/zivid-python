#include <Zivid/Calibration/HandEye.h>

#include <ZividPython/Calibrate.h>
#include <ZividPython/CalibrationResidual.h>
#include <ZividPython/Matrix.h>

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

namespace ZividPython
{
    void wrapClass(pybind11::class_<Zivid::Calibration::HandEyeOutput> pyClass)
    {
        pyClass.def("valid", &Zivid::Calibration::HandEyeOutput::valid)
            .def("handEyeTransform",
                 [](const Zivid::Calibration::HandEyeOutput &calibrationOutput) {
                     return Conversion::toPy(calibrationOutput.transform());
                 })
            .def("perPoseCalibrationResiduals", &Zivid::Calibration::HandEyeOutput::residuals);
    }

    void wrapClass(pybind11::class_<Zivid::Calibration::HandEyeInput> pyClass)
    {
        pyClass.def(py::init<Zivid::Calibration::Pose, Zivid::Calibration::DetectionResult>());
    }
} // namespace ZividPython
