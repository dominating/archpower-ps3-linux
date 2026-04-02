sed -i 's/AVFrame \*p = av_frame_alloc();/uint8_t *p_data[3]; int p_linesize[3];/g' ./ps3-remote-play/open-rp/orp.cpp
sed -i 's/p.data\[0\]/p_data[0]/g' ./ps3-remote-play/open-rp/orp.cpp
sed -i 's/p.data\[1\]/p_data[1]/g' ./ps3-remote-play/open-rp/orp.cpp
sed -i 's/p.data\[2\]/p_data[2]/g' ./ps3-remote-play/open-rp/orp.cpp
sed -i 's/p.linesize\[0\]/p_linesize[0]/g' ./ps3-remote-play/open-rp/orp.cpp
sed -i 's/p.linesize\[1\]/p_linesize[1]/g' ./ps3-remote-play/open-rp/orp.cpp
sed -i 's/p.linesize\[2\]/p_linesize[2]/g' ./ps3-remote-play/open-rp/orp.cpp
sed -i 's/p.data, p.linesize/p_data, p_linesize/g' ./ps3-remote-play/open-rp/orp.cpp
