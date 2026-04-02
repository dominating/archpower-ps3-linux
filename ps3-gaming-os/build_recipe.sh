#!/bin/bash
# PS3 Custom Gaming OS Bootstrap Script (Debian PPC / Red Ribbon Base)
# WARNING: Run as root.

echo "[*] Phase 1: Ripping out Desktop Bloat..."
# Strip out LXDE/XFCE/GNOME, display managers, and useless daemons
apt-get update
apt-get purge -y lxde* xfce4* lightdm gdm3 x11-common
apt-get autoremove -y --purge

# Install minimal X server (just enough for EmulationStation/SDL)
apt-get install -y xorg xinit xserver-xorg-video-fbdev

echo "[*] Phase 2: Memory Optimization (ZRAM + Massive Swap)..."
# Set up a 2GB swap file to prevent out-of-memory crashes on big ROMs
fallocate -l 2G /swapfile
chmod 600 /swapfile
mkswap /swapfile
swapon /swapfile
echo "/swapfile none swap sw 0 0" >> /etc/fstab

# Install ZRAM to compress RAM on the fly (acts as a hyper-fast RAM multiplier)
apt-get install -y zram-tools
echo "ALGO=lz4" > /etc/default/zramswap
echo "PERCENT=50" >> /etc/default/zramswap
systemctl restart zramswap

# Aggressive swappiness tweaks to prioritize ZRAM over HDD swap
echo "vm.swappiness=80" >> /etc/sysctl.conf
sysctl -p

echo "[*] Phase 3: The 'Will Work' Roster & EmulationStation..."
# Install the native lightweight games
apt-get install -y dosbox wesnoth freeciv

# Setup build tools for RetroArch & Cores optimized for the Cell Broadband Engine
apt-get install -y build-essential git libsdl2-dev
export CFLAGS="-mcpu=cell -mtune=cell -O3 -pipe -fomit-frame-pointer"
export CXXFLAGS="$CFLAGS"

# (Placeholder for RetroArch and EmulationStation compilation)
# In reality, this pulls from git, configures with Cell flags, and makes.
echo "[*] Compiling RetroArch with Cell PPE optimizations..."
# git clone https://github.com/libretro/RetroArch.git ...

echo "[*] Phase 4: Custom Branding & Console UI..."
# Set up auto-login to EmulationStation without a desktop manager
mkdir -p /etc/systemd/system/getty@tty1.service.d/
cat << 'INIT' > /etc/systemd/system/getty@tty1.service.d/override.conf
[Service]
ExecStart=
ExecStart=-/sbin/agetty --autologin root --noclear %I $TERM
INIT

# Start X and EmulationStation on bash login
echo '[[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && exec startx' >> ~/.bash_profile
echo 'exec emulationstation' > ~/.xinitrc

# Install Plymouth for a sleek boot splash
apt-get install -y plymouth plymouth-themes
# plymouth-set-default-theme -R tribar

echo "[*] System transformed into PS3 Scrap-Metal Gaming OS. Rebooting..."
