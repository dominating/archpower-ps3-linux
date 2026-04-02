sed -i 's/AVCodec \*codec/const AVCodec *codec/g' ./ps3-remote-play/open-rp/orp.cpp
sed -i 's/AVPicture p;/AVFrame *p = av_frame_alloc();/g' ./ps3-remote-play/open-rp/orp.cpp
