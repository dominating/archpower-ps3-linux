
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
    