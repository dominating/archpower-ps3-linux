#!/bin/bash
# Environment setup for PS3 toolchain
export PS3DEV=/usr/local/ps3dev
export PSL1GHT=$PS3DEV
export PATH=$PATH:$PS3DEV/bin:$PS3DEV/ppu/bin

# Build the project
make clean
make all
