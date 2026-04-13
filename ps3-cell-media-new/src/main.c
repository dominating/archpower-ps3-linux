#include <ppu-lv2.h>
#include <stdio.h>
#include <stdbool.h>
#include <malloc.h>
#include <string.h>
#include <unistd.h>
#include <curl/curl.h>
#include "cJSON.h"
#include <libavcodec/avcodec.h>
#include <libavformat/avformat.h>
#include <libswscale/swscale.h>
#include "jellyfin_api.h"

#include <tiny3d.h>
#include <libfont.h>
#include <io/pad.h>

#define WINDOW_WIDTH 848
#define WINDOW_HEIGHT 512

void libps3rp_decode_frame(AVCodecContext *dec_ctx, AVFrame *frame, AVPacket *pkt) {
    // Decoding logic via FFmpeg/libavcodec
}

void draw_rect(float x, float y, float w, float h, u32 rgba) {
    tiny3d_SetPolygon(TINY3D_QUADS);
    tiny3d_VertexPos(x, y, 1);
    tiny3d_VertexColor(rgba);
    tiny3d_VertexPos(x + w, y, 1);
    tiny3d_VertexColor(rgba);
    tiny3d_VertexPos(x + w, y + h, 1);
    tiny3d_VertexColor(rgba);
    tiny3d_VertexPos(x, y + h, 1);
    tiny3d_VertexColor(rgba);
    tiny3d_End();
}

int main(s32 argc, const char* argv[]) {
    printf("[Cell Media] Starting Jellyfin Client on PS3 (tiny3d + FFmpeg)...\n");

    JellyfinContext jf_ctx;
    jellyfin_init(&jf_ctx, "http://192.168.1.100:8096", "PS3_CELL_1", "PS3 Cell Media", "1.0.0");
    printf("[Cell Media] Jellyfin context initialized.\n");

    curl_global_init(CURL_GLOBAL_ALL);
#if LIBAVCODEC_VERSION_INT < AV_VERSION_INT(58, 9, 100)
    av_register_all();
#endif

    tiny3d_Init(1024*1024);
    ioPadInit(7);

    bool running = true;
    padInfo padinfo;
    padData paddata;

    while (running) {
        ioPadGetInfo(&padinfo);
        for(int i = 0; i < MAX_PORT_NUM; i++) {
            if(padinfo.status[i]) {
                ioPadGetData(i, &paddata);
                if(paddata.BTN_CIRCLE) {
                    running = false;
                }
            }
        }
        
        tiny3d_Clear(0x101019FF, TINY3D_CLEAR_ALL); // 16, 16, 25 background
        tiny3d_AlphaTest(1, 0x10, TINY3D_ALPHA_FUNC_GEQUAL);
        tiny3d_BlendFunc(1, TINY3D_BLEND_FUNC_SRC_RGB_SRC_ALPHA, TINY3D_BLEND_FUNC_SRC_RGB_ONE_MINUS_SRC_ALPHA, TINY3D_BLEND_RGB_FUNC_ADD);
        tiny3d_Project2D();

        // Draw a primitive UI box representing a movie cover (0, 164, 220)
        draw_rect(100.0f, 100.0f, 200.0f, 300.0f, 0x00A4DCFF);

        tiny3d_Flip();
    }

    jellyfin_cleanup(&jf_ctx);
    curl_global_cleanup();
    
    return 0;
}
