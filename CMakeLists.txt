cmake_minimum_required(VERSION 3.16)

project(the_anomlys LANGUAGES CXX VERSION 0.1.0)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_executable(the_anomlys
    src/main.cpp
)

target_compile_features(the_anomlys PRIVATE cxx_std_17)

if (MSVC)
    target_compile_options(the_anomlys PRIVATE /W4 /permissive-)
else()
    target_compile_options(the_anomlys PRIVATE -Wall -Wextra -Wpedantic)
endif()
