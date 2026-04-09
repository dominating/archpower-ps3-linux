# PS3 Darwin / XNU Kernel Port (Mac OS X on Cell)

## Project Goal
Boot Apple's open-source XNU kernel (PowerPC 32/64-bit, OS X 10.5 Leopard era) directly on the PS3 Cell Broadband Engine via Petitboot, bypassing Linux completely. 

## The Challenge
Apple's PowerPC kernels expect standard Apple hardware (OpenFirmware, Mac I/O controllers). The PS3 has none of this; it uses the Sony Level 1 (Lv1) Hypervisor. To make XNU boot, we must intercept every hardware call XNU makes and translate it into a PS3 Lv1 hypercall (`sc 1`).

## Architecture Roadmap

### 1. Bootloader Wrapper (`ps3_boot.c`)
Petitboot loads an ELF binary. We need a wrapper that:
- Receives the device tree from Petitboot.
- Initializes the PS3 Lv1 Hypervisor environment.
- Maps the XNU kernel into memory using `lv1_allocate_memory`.
- Jumps to the XNU kernel entry point (`_start`).

### 2. Hypervisor Call Interface (`lv1_calls.h`)
Replaces Apple's platform expert (PE) functions.
- Storage: Intercepts SATA/IDE requests and routes them to `lv1_storage_read`.
- Memory: Replaces Apple's HTAB (Hash Page Table) management with `lv1_write_htab_entry`.
- USB/Bluetooth: Bypasses standard OHCI/EHCI initialization to request control from Lv1.

### 3. SMP (Symmetric Multiprocessing)
The Cell has 1 PPE (with 2 threads) and 8 SPEs. XNU will see this as a dual-core PowerPC G5. We will initially disable SPEs and only bootstrap the main PPE threads.

## Next Steps
1. Fork Apple's `xnu-1228` (OS X 10.5) source code.
2. Strip out the `PE_mac_init` (Platform Expert) code.
3. Write `PE_ps3_init` using our custom Lv1 drivers.