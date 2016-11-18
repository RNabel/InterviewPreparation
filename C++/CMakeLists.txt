cmake_minimum_required(VERSION 3.6)
project(C__)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/ArrayVector)
add_subdirectory(ArrayVector)
