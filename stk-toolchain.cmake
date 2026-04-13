set(CMAKE_SYSTEM_NAME Generic)
set(CMAKE_SYSTEM_PROCESSOR powerpc64le) # PS3 Cell architecture
set(CMAKE_CROSSCOMPILING 1)

# Point to your toolchain path
set(CMAKE_C_COMPILER /usr/local/ps3dev/ppu/bin/ppu-gcc)
set(CMAKE_CXX_COMPILER /usr/local/ps3dev/ppu/bin/ppu-g++)
