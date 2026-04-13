#include <SDL2/SDL.h>
#include <stdio.h>
#include <stdbool.h>
#include <curl/curl.h>
#include "cJSON.h"
#include <libavcodec/avcodec.h>
#include <libavformat/avformat.h>
#include <libswscale/swscale.h>
#include "jellyfin_api.h"

#define WINDOW_WIDTH 1280
#define WINDOW_HEIGHT 720

// Simulate libps3rp integration
void libps3rp_decode_frame(AVCodecContext *dec_ctx, AVFrame *frame, AVPacket *pkt, SDL_Renderer *renderer, SDL_Texture *texture) {
    // Decoding logic via FFmpeg/libavcodec
    // In a real app, we'd avcodec_send_packet and avcodec_receive_frame here
    // Then use libswscale to convert YUV to RGB and update the texture
}

int main(int argc, char* argv[]) {
    printf("[Cell Media] Starting Jellyfin Client on PS3 (SDL2 + FFmpeg)...\n");

    JellyfinContext jf_ctx;
    jellyfin_init(&jf_ctx, "http://192.168.1.100:8096", "PS3_CELL_1", "PS3 Cell Media", "1.0.0");
    printf("[Cell Media] Jellyfin context initialized.\n");

    // Initialize libcurl
    curl_global_init(CURL_GLOBAL_ALL);

    // Initialize FFmpeg
#if LIBAVCODEC_VERSION_INT < AV_VERSION_INT(58, 9, 100)
    av_register_all();
#endif
    avformat_network_init();

    if (SDL_Init(SDL_INIT_VIDEO | SDL_INIT_JOYSTICK) < 0) {
        printf("[Cell Media] SDL could not initialize! SDL_Error: %s\n", SDL_GetError());
        return -1;
    }

    SDL_Window *window = SDL_CreateWindow("PS3 Jellyfin", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, WINDOW_WIDTH, WINDOW_HEIGHT, SDL_WINDOW_SHOWN);
    if (!window) {
        printf("[Cell Media] Window could not be created! SDL_Error: %s\n", SDL_GetError());
        SDL_Quit();
        return -1;
    }

    SDL_Renderer *renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);
    if (!renderer) {
        printf("[Cell Media] Renderer could not be created! SDL_Error: %s\n", SDL_GetError());
        SDL_DestroyWindow(window);
        SDL_Quit();
        return -1;
    }

    SDL_Texture *video_texture = SDL_CreateTexture(renderer, SDL_PIXELFORMAT_YV12, SDL_TEXTUREACCESS_STREAMING, WINDOW_WIDTH, WINDOW_HEIGHT);

    bool running = true;
    SDL_Event e;

    while (running) {
        while (SDL_PollEvent(&e) != 0) {
            if (e.type == SDL_QUIT) {
                running = false;
            } else if (e.type == SDL_JOYBUTTONDOWN) {
                if (e.jbutton.button == 13) { 
                    running = false;
                }
            }
        }
        
        // Clear background
        SDL_SetRenderDrawColor(renderer, 16, 16, 25, 255);
        SDL_RenderClear(renderer);
        
        // Draw a primitive UI box representing a movie cover
        SDL_Rect cover = { 100, 100, 200, 300 };
        SDL_SetRenderDrawColor(renderer, 0, 164, 220, 255);
        SDL_RenderFillRect(renderer, &cover);

        // libps3rp pipeline stub - we would normally decode and update texture
        // libps3rp_decode_frame(dec_ctx, frame, pkt, renderer, video_texture);
        // SDL_RenderCopy(renderer, video_texture, NULL, NULL);

        SDL_RenderPresent(renderer);
    }

    jellyfin_cleanup(&jf_ctx);
    SDL_DestroyTexture(video_texture);
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
    
    curl_global_cleanup();
    avformat_network_deinit();
    
    return 0;
}
