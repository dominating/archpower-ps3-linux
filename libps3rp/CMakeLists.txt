cmake_minimum_required(VERSION 3.10.2)

project(ps3rp-jni)

# Set the library name
set(LIBRARY_NAME ps3rp)

# Add our source files
add_library(${LIBRARY_NAME} SHARED
    src/ps3rp_jni.cpp
    src/ps3rp.cpp
    src/av_decoder.cpp
    src/stream_crypto.cpp
    src/auth_crypto_isolated.cpp
    src/base64.cpp
)

# Find JNI and Android Log libraries
find_package(JNI REQUIRED)
find_library(log-lib log)

# Include directories
target_include_directories(${LIBRARY_NAME} PRIVATE 
    ${JNI_INCLUDE_DIRS}
    include
)

# Link everything together
target_link_libraries(${LIBRARY_NAME}
    ${log-lib}
    # Add other required system libraries here, e.g., z, m, etc.
)

# Ensure visibility
set_target_properties(${LIBRARY_NAME} PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/libs/${ANDROID_ABI}"
)
