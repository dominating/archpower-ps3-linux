cat << 'REPL' > rep_vid.txt
		int ret = avcodec_send_packet(context, &packet->pkt);
		bytes_decoded = -1;
		frame_done = 0;
		if (ret >= 0) {
			ret = avcodec_receive_frame(context, frame);
			if (ret >= 0) {
				frame_done = 1;
				bytes_decoded = packet->pkt.size;
			}
		}
REPL
cat << 'REPL2' > rep_aud.txt
		int ret = avcodec_send_packet(context, &packet->pkt);
		bytes_decoded = -1;
		frame_size = 0;
		if (ret >= 0) {
			AVFrame *aframe = av_frame_alloc();
			ret = avcodec_receive_frame(context, aframe);
			if (ret >= 0) {
				int data_size = av_samples_get_buffer_size(NULL, context->ch_layout.nb_channels, aframe->nb_samples, context->sample_fmt, 1);
				if (data_size < 0) {
					data_size = av_samples_get_buffer_size(NULL, context->channels, aframe->nb_samples, context->sample_fmt, 1);
				}
				frame_size = data_size;
				memcpy(buffer, aframe->data[0], data_size);
				bytes_decoded = packet->pkt.size;
			}
			av_frame_free(&aframe);
		}
REPL2
