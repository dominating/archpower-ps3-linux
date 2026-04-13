#include "lv1_calls.h"
#include "boot_args.h"
#include <stdint.h>

extern void _xnu_start(boot_args *args); // Entry point of the Apple XNU Kernel

// We statically allocate boot_args so it resides in the BSS section
static boot_args ps3_boot_args;

void _start(uint64_t boot_id, uint64_t client_id, uint64_t device_tree) {
    // Avoid compiler unused parameter warnings
    (void)boot_id;
    (void)client_id;

    ps3_print("\n\n==========================================\n");
    ps3_print("   PS3 XNU Darwin Bootloader Initialized\n");
    ps3_print("==========================================\n");

    ps3_print("[*] Parsing Petitboot device tree...\n");

    ps3_print("[*] Requesting Memory Mapping from Lv1...\n");
    uint64_t memory_base = 0;
    // LV1_ALLOCATE_MEMORY needs memory_base as output, but for now we simulate
    uint64_t status = lv1_hypercall(LV1_ALLOCATE_MEMORY, 256 * 1024 * 1024, 0, 0, 0, 0, 0, 0); 
    
    if (status != 0) {
        ps3_print("[!] FATAL: Failed to allocate memory from Lv1 Hypervisor.\n");
        while(1);
    }

    ps3_print("[*] Lv1 Memory Allocated successfully.\n");
    ps3_print("[*] Constructing XNU boot_args payload...\n");

    // Populate the XNU boot_args structure
    ps3_boot_args.version = 1;
    ps3_boot_args.revision = 1;
    ps3_boot_args.device_tree = device_tree;
    ps3_boot_args.device_tree_size = 0; // TODO: Parse FDT size
    ps3_boot_args.memory_map = memory_base;
    ps3_boot_args.memory_map_size = 256 * 1024 * 1024;
    
    // Set basic framebuffer info (Cell RSX default text mode assumption)
    ps3_boot_args.video_base_addr = 0x0; // To be mapped via Lv1 RSX setup
    ps3_boot_args.video_width = 1280;
    ps3_boot_args.video_height = 720;
    ps3_boot_args.video_depth = 32;
    
    // Pass fake command line
    const char *cmd = "-v debug=0x144";
    char *dst = ps3_boot_args.command_line;
    while (*cmd) *dst++ = *cmd++;
    *dst = '\0';

    ps3_print("[*] Jumping to XNU mach_kernel entry point...\n");
    
    // Jump to the Apple kernel, passing the boot_args pointer
    _xnu_start(&ps3_boot_args);
    
    while(1);
}
