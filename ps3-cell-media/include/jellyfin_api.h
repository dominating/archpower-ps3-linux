#ifndef JELLYFIN_API_H
#define JELLYFIN_API_H

#include <stdint.h>
#include <stdbool.h>

#define JELLYFIN_MAX_URL_LEN 256
#define JELLYFIN_MAX_TOKEN_LEN 256
#define JELLYFIN_MAX_ERR_LEN 256

typedef struct {
    char server_url[JELLYFIN_MAX_URL_LEN];
    char access_token[JELLYFIN_MAX_TOKEN_LEN];
    char user_id[64];
    char device_id[64];
    char client_name[64];
    char client_version[32];
    char last_error[JELLYFIN_MAX_ERR_LEN];
} JellyfinContext;

// Initialize the context
void jellyfin_init(JellyfinContext *ctx, const char *server_url, const char *device_id, const char *client_name, const char *client_version);

// Authenticate with the server
bool jellyfin_login(JellyfinContext *ctx, const char *username, const char *password);

// Example to get items (returns raw JSON string, caller must free)
char* jellyfin_get_items(JellyfinContext *ctx, const char *parent_id);

// Cleanup any internal state if needed
void jellyfin_cleanup(JellyfinContext *ctx);

#endif // JELLYFIN_API_H
