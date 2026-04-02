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

extern "C" JNIEXPORT jint JNICALL
Java_com_example_ps3rp_PS3RPClient_receive(JNIEnv *env, jobject thiz, jbyteArray buffer) {
    if (!g_client) return -1;
    jsize len = env->GetArrayLength(buffer);
    jbyte* native_buffer = env->GetByteArrayElements(buffer, 0);
    int received = g_client->receive(reinterpret_cast<uint8_t*>(native_buffer), len);
    env->ReleaseByteArrayElements(buffer, native_buffer, 0);
    return received;
}
