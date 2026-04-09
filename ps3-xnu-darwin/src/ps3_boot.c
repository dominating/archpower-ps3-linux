#include "lv1_calls.h"
#include <stdint.h>

// This wrapper is the ELF entry point loaded by Petitboot.
// It sets up the hypervisor environment before jumping into the actual XNU mach kernel.

extern void _xnu_start(void); // Entry point of the Apple XNU Kernel

void _start(uint64_t boot_id, uint64_t client_id, uint64_t device_tree) {
    // 1. Initialize PS3 Hypervisor Console
    ps3_print("\n\n==========================================\n");
    ps3_print("   PS3 XNU Darwin Bootloader Initialized\n");
    ps3_print("==========================================\n");

    ps3_print("[*] Parsing Petitboot device tree...\n");
    // TODO: Parse the flattened device tree (FDT) passed from Petitboot

    ps3_print("[*] Requesting Memory Mapping from Lv1...\n");
    // Ask Sony's Hypervisor for RAM. 
    // XNU needs a contiguous block for the Mach-O kernel segments.
    uint64_t memory_base = 0;
    uint64_t status = lv1_hypercall(LV1_ALLOCATE_MEMORY, 256 * 1024 * 1024, 0, 0, 0, 0, 0, 0); // 256MB
    
    if (status != 0) {
        ps3_print("[!] FATAL: Failed to allocate memory from Lv1 Hypervisor.\n");
        while(1); // Halt
    }

    ps3_print("[*] Lv1 Memory Allocated successfully.\n");
    ps3_print("[*] Patching XNU Platform Expert (PE) structures...\n");

    // TODO: Here we map the XNU structures to bypass OpenFirmware checks.
    // Instead of looking for Apple hardware, XNU will call our Lv1 wrappers.

    ps3_print("[*] Jumping to XNU mach_kernel entry point...\n");
    
    // Jump to the Apple kernel
    _xnu_start();
    
    // We should never return here.
    while(1);
}
