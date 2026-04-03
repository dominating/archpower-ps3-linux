#include "../include/av_decoder.h"
#include <iostream>

namespace ps3rp {

AVDecoder::AVDecoder(CodecType type) 
    : m_type(type), m_codec_ctx(nullptr), m_codec(nullptr), m_frame(nullptr), m_packet(nullptr) 
{
}

AVDecoder::~AVDecoder() 
{
    if (m_codec_ctx) {
        avcodec_free_context(&m_codec_ctx);
    }
    if (m_frame) {
        av_frame_free(&m_frame);
    }
    if (m_packet) {
        av_packet_free(&m_packet);
    }
}

bool AVDecoder::init(int channels, int sample_rate, int bit_rate) 
{
    AVCodecID codec_id;
    switch (m_type) {
        case CodecType::VIDEO_H264: codec_id = AV_CODEC_ID_H264; break;
        case CodecType::VIDEO_MPEG4: codec_id = AV_CODEC_ID_MPEG4; break;
        case CodecType::AUDIO_AAC: codec_id = AV_CODEC_ID_AAC; break;
        case CodecType::AUDIO_ATRAC3: codec_id = AV_CODEC_ID_ATRAC3; break;
        default: return false;
    }

    m_codec = avcodec_find_decoder(codec_id);
    if (!m_codec) {
        std::cerr << "Could not find decoder for codec ID: " << codec_id << std::endl;
        return false;
    }

    m_codec_ctx = avcodec_alloc_context3(m_codec);
    if (!m_codec_ctx) {
        return false;
    }

    if (m_type == CodecType::AUDIO_AAC || m_type == CodecType::AUDIO_ATRAC3) {
        m_codec_ctx->channels = channels;
        m_codec_ctx->sample_rate = sample_rate;
        m_codec_ctx->bit_rate = bit_rate;
    }

    if (avcodec_open2(m_codec_ctx, m_codec, nullptr) < 0) {
        std::cerr << "Could not open codec." << std::endl;
        avcodec_free_context(&m_codec_ctx);
        return false;
    }

    m_frame = av_frame_alloc();
    m_packet = av_packet_alloc();

    return true;
}

std::vector<AVFrame*> AVDecoder::decode(const uint8_t* data, size_t size) 
{
    std::vector<AVFrame*> decoded_frames;
    if (!m_codec_ctx || !m_frame || !m_packet) return decoded_frames;

    m_packet->data = const_cast<uint8_t*>(data);
    m_packet->size = size;

    int ret = avcodec_send_packet(m_codec_ctx, m_packet);
    if (ret < 0) {
        std::cerr << "Error sending packet to decoder" << std::endl;
        return decoded_frames;
    }

    while (ret >= 0) {
        ret = avcodec_receive_frame(m_codec_ctx, m_frame);
        if (ret == AVERROR(EAGAIN) || ret == AVERROR_EOF) {
            break;
        } else if (ret < 0) {
            std::cerr << "Error during decoding" << std::endl;
            break;
        }

        AVFrame* out_frame = av_frame_clone(m_frame);
        if (out_frame) {
            decoded_frames.push_back(out_frame);
        }
    }

    return decoded_frames;
}

} // namespace ps3rp
