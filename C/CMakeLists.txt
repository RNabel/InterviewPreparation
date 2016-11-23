cmake_minimum_required(VERSION 3.6)
project(C)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Werror")

add_subdirectory(ArrayVector)
add_subdirectory(HashTable)
add_subdirectory(Search)
