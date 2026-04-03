#ifndef PS3RP_AV_DECODER_H
#define PS3RP_AV_DECODER_H

#include <memory>
#include <vector>

extern "C" {
#include <libavcodec/avcodec.h>
#include <libavutil/frame.h>
}

namespace ps3rp {

class AVDecoder {
public:
    enum class CodecType {
        VIDEO_H264,
        VIDEO_MPEG4,
        AUDIO_AAC,
        AUDIO_ATRAC3
    };

    AVDecoder(CodecType type);
    ~AVDecoder();

    bool init(int channels = 0, int sample_rate = 0, int bit_rate = 0);
    
    // Returns a vector of decoded AVFrames. The caller is responsible for freeing them using av_frame_free()
    // Alternatively we can copy data out or use smart pointers, but returning raw AVFrame pointers is common for FFmpeg wrappers
    std::vector<AVFrame*> decode(const uint8_t* data, size_t size);

private:
    CodecType m_type;
    AVCodecContext* m_codec_ctx;
    const AVCodec* m_codec;
    AVFrame* m_frame;
    AVPacket* m_packet;
};

} // namespace ps3rp

#endif // PS3RP_AV_DECODER_H
