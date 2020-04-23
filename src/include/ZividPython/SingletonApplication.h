#pragma once

#include <Zivid/Application.h>
#include <ZividPython/Releasable.h>
#include <ZividPython/ReleasableCamera.h>
#include <ZividPython/Wrappers.h>

namespace ZividPython
{
    class SingletonApplication : public Singleton<Zivid::Application>
    {
    public:
        ZIVID_PYTHON_FORWARD_0_ARGS_WRAP_CONTAINER_RETURN(std::vector, ReleasableCamera, cameras)

//        ZIVID_PYTHON_FORWARD_1_ARGS_WRAP_RETURN(ReleasableCamera, connectCamera, const Zivid::Settings &, setting)
//
//        ZIVID_PYTHON_FORWARD_2_ARGS_WRAP_RETURN(ReleasableCamera,
//                                                connectCamera,
//                                                const Zivid::SerialNumber &,
//                                                serialNumber,
//                                                const Zivid::Settings &,
//                                                setting)
//
//        ZIVID_PYTHON_FORWARD_2_ARGS_WRAP_RETURN(ReleasableCamera,
//                                                createFileCamera,
//                                                const std::string &,
//                                                fileName,
//                                                const Zivid::Settings &,
//                                                setting)
    };

    void wrapClass(pybind11::class_<SingletonApplication> pyClass);
} // namespace ZividPython
