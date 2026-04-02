cmake_minimum_required(VERSION 3.10)
project(libps3rp)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

find_package(OpenSSL REQUIRED)
find_package(JNI)

include_directories(include ${OPENSSL_INCLUDE_DIR})
if(JNI_FOUND)
    include_directories(${JNI_INCLUDE_DIRS})
else()
    # Stub JNI headers for CI/Verification without JDK
    file(WRITE ${CMAKE_BINARY_DIR}/jni.h "
        #ifndef JNI_STUB_H
        #define JNI_STUB_H
        #include <cstdint>
        typedef void* JNIEnv;
        typedef void* jobject;
        typedef void* jstring;
        typedef void* jbyteArray;
        typedef int jint;
        typedef int jsize;
        typedef unsigned char jboolean;
        typedef signed char jbyte;
        #define JNI_TRUE 1
        #define JNI_FALSE 0
        #define JNICALL
        #define JNIEXPORT
        #endif
    ")
    include_directories(${CMAKE_BINARY_DIR})
endif()

# Shared Library
add_library(ps3rp SHARED 
    src/ps3rp.cpp 
    src/base64.cpp 
    src/auth_crypto_isolated.cpp 
    src/stream_crypto.cpp
    src/ps3rp_jni.cpp
)

target_link_libraries(ps3rp ${OPENSSL_CRYPTO_LIBRARY})
