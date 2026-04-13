CC = ppu-gcc
LD = ppu-ld
OBJCOPY = ppu-objcopy

CFLAGS = -m64 -ffreestanding -fno-builtin -nostdlib -mbig -I./include -O2 -Wall -Wextra -fno-pic -fno-pie
LDFLAGS = -T linker.ld -nostdlib -melf64ppc

SRCS = src/ps3_boot.c src/PE_ps3.c src/xnu_stub.c
OBJS = $(SRCS:.c=.o)

all: xnu_ps3.elf xnu_ps3.bin

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

xnu_ps3.elf: $(OBJS)
	$(LD) $(LDFLAGS) $(OBJS) -o $@

xnu_ps3.bin: xnu_ps3.elf
	$(OBJCOPY) -O binary $< $@

clean:
	rm -f $(OBJS) xnu_ps3.elf xnu_ps3.bin
