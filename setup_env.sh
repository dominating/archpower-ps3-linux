#!/bin/bash
set -e

# Setup PSL1GHT and ps3toolchain environment variables
export PS3DEV=/usr/local/ps3dev
export PSL1GHT=$PS3DEV/psl1ght
export PATH=$PATH:$PS3DEV/bin:$PS3DEV/ppu/bin:$PS3DEV/spu/bin

echo "Environment variables set."
echo "export PS3DEV=$PS3DEV"
echo "export PSL1GHT=$PSL1GHT"
echo "export PATH=\$PATH:\$PS3DEV/bin:\$PS3DEV/ppu/bin:\$PS3DEV/spu/bin"

echo "Cloning modern ps3toolchain..."
git clone https://github.com/ps3dev/ps3toolchain.git || true
cd ps3toolchain
echo "To build the toolchain, run: ./toolchain.sh"
cd ..

echo "Cloning modern PSL1GHT..."
git clone https://github.com/ps3dev/PSL1GHT.git || true
cd PSL1GHT
echo "To build PSL1GHT, run: make install-ctrl && make && make install"
cd ..

echo "Cloning ps3libraries (includes SDL2)..."
git clone https://github.com/ps3dev/ps3libraries.git || true
cd ps3libraries
echo "To build libraries including SDL2, run: ./libraries.sh"

echo "Setup script completed. Ensure to add variables to your .bashrc and run the respective build scripts."
