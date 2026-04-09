#!/bin/bash
# Fetch Apple XNU Kernel Source (OS X 10.5 Leopard era)

XNU_VERSION="xnu-1228"
APPLE_OSS_URL="https://opensource.apple.com/tarballs/xnu/${XNU_VERSION}.tar.gz"

echo "[*] Downloading Apple open-source XNU kernel (${XNU_VERSION})..."
curl -O $APPLE_OSS_URL

echo "[*] Extracting..."
tar -xzf ${XNU_VERSION}.tar.gz

echo "[*] Cleaning up..."
rm ${XNU_VERSION}.tar.gz

echo "[*] XNU source extracted to ${XNU_VERSION}/"
echo "[*] Next step: Injecting PE_ps3.c into the osfmk/pexpert/ hierarchy."
