#ifndef _PS3_LV1_CALLS_H
#define _PS3_LV1_CALLS_H

#include <stdint.h>

// LV1 Hypercall Definitions
// On PS3 PowerPC, a hypercall is invoked using the 'sc 1' instruction.

static inline uint64_t lv1_hypercall(uint64_t op, uint64_t in1, uint64_t in2, uint64_t in3, uint64_t in4, uint64_t in5, uint64_t in6, uint64_t in7) {
    register uint64_t r11 __asm__("11") = op;
    register uint64_t r3 __asm__("3") = in1;
    register uint64_t r4 __asm__("4") = in2;
    register uint64_t r5 __asm__("5") = in3;
    register uint64_t r6 __asm__("6") = in4;
    register uint64_t r7 __asm__("7") = in5;
    register uint64_t r8 __asm__("8") = in6;
    register uint64_t r9 __asm__("9") = in7;

    __asm__ volatile ("sc 1"
                      : "+r"(r3), "+r"(r4), "+r"(r5), "+r"(r6), "+r"(r7), "+r"(r8), "+r"(r9)
                      : "r"(r11)
                      : "r0", "r10", "r12", "memory", "cc");
    return r3;
}

// Memory Management
#define LV1_ALLOCATE_MEMORY 2
#define LV1_WRITE_HTAB_ENTRY 28

// Storage (SATA/Flash)
#define LV1_STORAGE_READ 234
#define LV1_STORAGE_WRITE 235

// USB/PCI Bus
#define LV1_MAP_DEVICE_MMIO 145

// TTY / Console (for kernel panic/debug output over Lv1)
#define LV1_PUT_CHAR 122

static inline void ps3_put_char(char c) {
    lv1_hypercall(LV1_PUT_CHAR, c, 0, 0, 0, 0, 0, 0);
}

static inline void ps3_print(const char* str) {
    while(*str) {
        ps3_put_char(*str++);
    }
}

#endif
