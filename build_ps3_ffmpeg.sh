#!/bin/bash
set -e

# Setup environment variables
export PS3DEV=/home/micemeat/.openclaw/workspace/ps3dev/ps3dev
export PSL1GHT=$PS3DEV
export PATH=$PATH:$PS3DEV/bin:$PS3DEV/ppu/bin:$PS3DEV/spu/bin

export CC=ppu-gcc
export CXX=ppu-g++
export AR=ppu-ar
export RANLIB=ppu-ranlib
export STRIP=ppu-strip

WORKSPACE=/home/micemeat/.openclaw/workspace
LIBAV_DIR=$WORKSPACE/libav-movian
BUILD_DIR=$WORKSPACE/ps3_ffmpeg_build
PORTLIBS_DIR=$PS3DEV/portlibs/ppu

# Create nostrictansi.h as it's required by Movian's patches/flags
mkdir -p $BUILD_DIR
cat << 'EOF' > $BUILD_DIR/nostrictansi.h
#undef __STRICT_ANSI__
EOF

cd $LIBAV_DIR

# Clean if previously built
[ -f Makefile ] && make distclean || true

LIBAV_COMMON_FLAGS="--disable-encoders --disable-filters --disable-muxers --disable-devices \
  --disable-demuxer=rtp --disable-protocol=rtp --disable-bzlib \
  --disable-decoder=twinvq --disable-decoder=snow --disable-decoder=cavs \
  --disable-ffmpeg --disable-ffplay --disable-ffprobe --disable-ffserver --disable-avfilter --disable-doc \
  --enable-decoder=png --enable-decoder=mjpeg \
  --enable-encoder=mjpeg --enable-encoder=png \
  --enable-muxer=spdif --enable-encoder=ac3 --enable-encoder=eac3 \
  --enable-muxer=matroska --enable-encoder=ffvhuff --enable-encoder=pcm_s16le"

# We must avoid --malloc-prefix=my for standard PSL1GHT use if they want to link standardly,
# but if the user wants Movian's exact extraction, let's keep it mostly similar but remove
# the malloc prefix just in case unless Movian specifically patched that malloc.
# Actually, PSL1GHT standard apps probably prefer the default malloc.
LIBAV_ARCH_FLAGS="--cross-prefix=ppu- --enable-cross-compile --arch=powerpc64 --cpu=cell --target-os=none --disable-shared --enable-static"

LIBAV_CFLAGS="-O2 -mminimal-toc -I${PSL1GHT}/target/include -B${PSL1GHT}/target/lib -B${PS3DEV}/host/ppu/lib -I${PS3DEV}/host/ppu/include -include $BUILD_DIR/nostrictansi.h"

echo "Configuring FFmpeg/libav for PS3..."
./configure \
  --prefix=$PORTLIBS_DIR \
  $LIBAV_ARCH_FLAGS \
  $LIBAV_COMMON_FLAGS \
  --extra-cflags="$LIBAV_CFLAGS" \
  --cc="ppu-gcc" || { echo "Configure failed, see config.log"; cat config.log; exit 1; }

echo "Building FFmpeg/libav for PS3..."
make -j$(nproc)

echo "Installing FFmpeg/libav to $PORTLIBS_DIR..."
make install

echo "Done! Static libraries should be in $PORTLIBS_DIR/lib"
