#include <ZividPython/ReleasableImage.h>

#include <pybind11/pybind11.h>

namespace py = pybind11;

namespace
{
    py::buffer_info makeBufferInfo(ZividPython::ReleasableImage &image)
    {
        const auto data = image.impl().data(); // todo: fix imple
        //auto dataArray = image.impl().copyData<Zivid::ColorRGBA>(); // double copy, both here and when returning buffer_info
        //// try to use latest pybind11 to get around const data pointers https://github.com/pybind/pybind11/issues/1993
        //auto * data = const_cast<Zivid::PointXYZColorRGBA*>(dataArray.data()); 
//
        ////using NativeDataType = decltype(data);
        using NativeDataType = std::remove_pointer_t<decltype(data)>;

        return py::buffer_info{
            const_cast<std::remove_const_t<std::remove_pointer_t<decltype(data)>>*>(
                data), // TODO: Const casting this until pybind11 has newer version than 2.4.3 has been released
            sizeof(Zivid::ColorRGBA),
            py::format_descriptor<Zivid::ColorRGBA>::format(),
            2,
            { image.height(), image.width() },
            { sizeof(Zivid::ColorRGBA) * image.width(), sizeof(Zivid::ColorRGBA) }
        };
//auto my_vec = std::vector<int>{};
//return py::buffer_info{ my_vec.data(),
//                                sizeof(int),
//                                py::format_descriptor<int>::format(),
//                                2,
//                                {0, 0 },
//                                {sizeof(int), sizeof(int)} };
    }
} // namespace

namespace ZividPython
{
    void wrapClass(pybind11::class_<ReleasableImage> pyClass)
    {
        PYBIND11_NUMPY_DTYPE(Zivid::ColorRGBA, r, g, b, a);

        pyClass.def_buffer(makeBufferInfo)
            .def("save", &ReleasableImage::save, py::arg("file_name"))
            .def("width", &ReleasableImage::width)
            .def("height", &ReleasableImage::height);
    }
} // namespace ZividPython
