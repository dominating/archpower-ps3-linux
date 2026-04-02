import os, sys, shutil

lib_dir = "libps3rp"

api_header = """#ifndef PS3RP_H
#define PS3RP_H

#include <string>
#include <vector>
#include <cstdint>

namespace ps3rp {

class Client {
public:
    Client();
    ~Client();
    bool init();
    bool connect(const std::string& ip, const std::string& pin);
    int receive(uint8_t* buffer, int max_size);
};

} // namespace ps3rp

#endif // PS3RP_H
"""
with open(os.path.join(lib_dir, "include", "ps3rp.h"), "w") as f:
    f.write(api_header)

api_src = """#include "ps3rp.h"
#include <iostream>

namespace ps3rp {

Client::Client() {}
Client::~Client() {}

bool Client::init() {
    std::cout << "PS3RP Client Init" << std::endl;
    return true;
}

bool Client::connect(const std::string& ip, const std::string& pin) {
    std::cout << "PS3RP Client Connect: " << ip << std::endl;
    return true;
}

int Client::receive(uint8_t* buffer, int max_size) {
    return 0;
}

} // namespace ps3rp
"""
with open(os.path.join(lib_dir, "src", "ps3rp.cpp"), "w") as f:
    f.write(api_src)

jni_src = """#include <jni.h>
#include "ps3rp.h"
#include <memory>

static std::unique_ptr<ps3rp::Client> g_client;

extern "C" JNIEXPORT jboolean JNICALL
Java_com_example_ps3rp_PS3RPClient_init(JNIEnv *env, jobject thiz) {
    g_client = std::make_unique<ps3rp::Client>();
    return g_client->init() ? JNI_TRUE : JNI_FALSE;
}

extern "C" JNIEXPORT jboolean JNICALL
Java_com_example_ps3rp_PS3RPClient_connect(JNIEnv *env, jobject thiz, jstring ip, jstring pin) {
    if (!g_client) return JNI_FALSE;
    const char *native_ip = env->GetStringUTFChars(ip, 0);
    const char *native_pin = env->GetStringUTFChars(pin, 0);
    bool res = g_client->connect(native_ip, native_pin);
    env->ReleaseStringUTFChars(ip, native_ip);
    env->ReleaseStringUTFChars(pin, native_pin);
    return res ? JNI_TRUE : JNI_FALSE;
}

extern "C" JNIEXPORT jint JNICALL
Java_com_example_ps3rp_PS3RPClient_receive(JNIEnv *env, jobject thiz, jbyteArray buffer) {
    if (!g_client) return -1;
    jsize len = env->GetArrayLength(buffer);
    jbyte* native_buffer = env->GetByteArrayElements(buffer, 0);
    int received = g_client->receive(reinterpret_cast<uint8_t*>(native_buffer), len);
    env->ReleaseByteArrayElements(buffer, native_buffer, 0);
    return received;
}
"""
with open(os.path.join(lib_dir, "src", "ps3rp_jni.cpp"), "w") as f:
    f.write(jni_src)

# Copy jni header for build to pass without jdk installed
# wait, JNI might not be found. Let's make sure find_package(JNI) is handled or stubbed
cmake_lists = """cmake_minimum_required(VERSION 3.10)
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
"""
with open(os.path.join(lib_dir, "CMakeLists.txt"), "w") as f:
    f.write(cmake_lists)

