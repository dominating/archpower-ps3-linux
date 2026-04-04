#!/bin/bash
set -e

echo "Building Bootable USB Structure for PS3 (Petitboot)"
mkdir -p usb_boot/live

# 1. Compress rootfs into squashfs
if command -v mksquashfs &> /dev/null; then
    echo "Compressing rootfs to SquashFS..."
    mksquashfs rootfs/ usb_boot/live/filesystem.squashfs -comp xz -b 1048576 -noappend
else
    echo "Warning: mksquashfs not found, skipping squashfs creation."
    echo "Install squashfs-tools to compress the live filesystem."
fi

# 2. Extract Kernel and Initrd from rootfs (if they exist)
echo "Looking for kernel and initrd..."
if ls rootfs/boot/vmlinu* 1> /dev/null 2>&1; then
    cp -v rootfs/boot/vmlinu* usb_boot/vmlinux
else
    echo "Notice: No vmlinux found in rootfs/boot/. You'll need a PS3-compatible kernel."
    touch usb_boot/vmlinux_placeholder
fi

if ls rootfs/boot/initrd* 1> /dev/null 2>&1; then
    cp -v rootfs/boot/initrd* usb_boot/initrd.img
else
    echo "Notice: No initrd found in rootfs/boot/."
    touch usb_boot/initrd_placeholder.img
fi

# 3. Generate kboot.conf
echo "Generating kboot.conf for Petitboot..."
cat << 'EOF' > usb_boot/kboot.conf
default=scrapmetal-live
timeout=10

scrapmetal-live='/vmlinux initrd=/initrd.img boot=live config quiet splash ps3fb=720p --'
scrapmetal-safemode='/vmlinux initrd=/initrd.img boot=live config nomodeset ps3fb=safe --'
scrapmetal-install='/vmlinux initrd=/initrd.img boot=live config installer ps3fb=720p --'
EOF

echo "======================================"
echo "USB Boot structure ready in 'usb_boot/' directory."
echo "To boot on PS3 via Petitboot:"
echo "1. Format a USB drive to FAT32."
echo "2. Copy everything inside 'usb_boot/' to the ROOT of the USB drive."
echo "3. Make sure you replace placeholders with a real PS3 kernel (vmlinux) and initrd if missing."
echo "4. Plug into PS3, load OtherOS/Petitboot, and select 'scrapmetal-live'."
echo "======================================"
