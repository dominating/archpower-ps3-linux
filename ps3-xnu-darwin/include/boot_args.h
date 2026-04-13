#ifndef _PS3_BOOT_ARGS_H
#define _PS3_BOOT_ARGS_H

#include <stdint.h>

#define BOOT_LINE_LENGTH 256

// Apple XNU boot_args structure (adapted for PowerPC/PS3)
typedef struct {
    uint16_t version;
    uint16_t revision;
    uint32_t reserved;
    uint64_t memory_map;
    uint32_t memory_map_size;
    uint32_t memory_map_descriptor_size;
    uint64_t device_tree;
    uint32_t device_tree_size;
    char     command_line[BOOT_LINE_LENGTH];
    uint64_t video_base_addr;
    uint32_t video_width;
    uint32_t video_height;
    uint32_t video_depth;
    uint32_t video_row_bytes;
} boot_args;

#endif
