#include <ZividPython/Matrix.h>
#include <ZividPython/Pose.h>

#include <pybind11/pybind11.h>

namespace py = pybind11;

namespace ZividPython
{
    void wrapClass(pybind11::class_<Zivid::Calibration::Pose> pyClass)
    {
        pyClass.def(py::init([](const Eigen::Matrix<float, 4, 4, Eigen::RowMajor> &matrix) {
            return std::make_unique<Zivid::Calibration::Pose>(Conversion::toCpp(matrix));
        }));
    }
} // namespace ZividPython
