#include <jni.h>
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

extern "C" JNIEXPORT jboolean JNICALL
Java_com_example_ps3rp_PS3RPClient_sendInput(JNIEnv *env, jobject thiz, jbyteArray inputData) {
    if (!g_client) return JNI_FALSE;
    jsize len = env->GetArrayLength(inputData);
    jbyte* native_data = env->GetByteArrayElements(inputData, 0);
    
    // Direct input bridge to PS3
    bool res = g_client->sendInput(reinterpret_cast<uint8_t*>(native_data), len);
    
    env->ReleaseByteArrayElements(inputData, native_data, 0);
    return res ? JNI_TRUE : JNI_FALSE;
}

extern "C" JNIEXPORT jint JNICALL
Java_com_example_ps3rp_PS3RPClient_decodeFrame(JNIEnv *env, jobject thiz, jobject buffer, jint offset, jint length) {
    if (!g_client) return -1;
    
    // Get direct access to Android MediaCodec buffer
    void* native_buffer = env->GetDirectBufferAddress(buffer);
    if (!native_buffer) return -1;
    
    // Decode frame directly into the provided memory block
    // This allows the PS3 data stream to be processed by Android hardware decoders
    int decoded = g_client->decodeFrame(reinterpret_cast<uint8_t*>(native_buffer) + offset, length);
    
    return decoded;
}

