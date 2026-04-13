#include "lv1_calls.h"
#include "boot_args.h"

// This acts as the fake mach_kernel for now, simulating XNU receiving the handoff
void _xnu_start(boot_args *args) {
    ps3_print("\n[XNU] mach_kernel entry point reached!\n");
    
    if (args->version == 1) {
        ps3_print("[XNU] Valid boot_args structure detected.\n");
    } else {
        ps3_print("[XNU] Invalid boot_args structure!\n");
    }
    
    ps3_print("[XNU] Boot args command line: ");
    ps3_print(args->command_line);
    ps3_print("\n");

    ps3_print("[XNU] Halting stub kernel execution.\n");
    while(1);
}
