cmake_minimum_required(VERSION 3.6)
project(C)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Werror")

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/ArrayVector)
add_subdirectory(ArrayVector)
