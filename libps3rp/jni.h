#ifndef JNI_STUB_H
#define JNI_STUB_H

#include <cstdint>

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

struct JNIEnv {
    const char* GetStringUTFChars(jstring, jboolean*) { return ""; }
    void ReleaseStringUTFChars(jstring, const char*) {}
    jsize GetArrayLength(jbyteArray) { return 0; }
    jbyte* GetByteArrayElements(jbyteArray, jboolean*) { return nullptr; }
    void ReleaseByteArrayElements(jbyteArray, jbyte*, jint) {}
};

#endif
