#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cjson/cJSON.h>

typedef struct {
    char server_url[256];
    char device_id[64];
    char client_name[64];
    char client_version[32];
    char access_token[256];
    char user_id[64];
    char last_error[256];
} JellyfinContext;

void jellyfin_init(JellyfinContext *ctx, const char *server_url, const char *device_id, const char *client_name, const char *client_version) {
    printf("[API] Initializing Jellyfin context...\n");
}

void jellyfin_cleanup(JellyfinContext *ctx) {
    printf("[API] Cleaning up context.\n");
}

void init_hardware_decoders() {
    printf("[System] Hardware decoders ready.\n");
}

char* jellyfin_get_items_native(const char* host, int port, const char* path) {
    printf("[Net] Native network calls stubbed for current build.\n");
    return strdup("{\"Items\": []}");
}

