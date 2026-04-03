#include <iostream>
#include <string>
#include <vector>
#include <thread>
#include <chrono>

#include "ps3rp.h"
#include "av_decoder.h"

int main(int argc, char* argv[]) {
    if (argc < 3) {
        std::cerr << "Usage: " << argv[0] << " <ip> <pin>\n";
        return 1;
    }

    std::string ip = argv[1];
    std::string pin = argv[2];

    std::cout << "Starting PS3RP Test Client...\n";
    std::cout << "Target IP: " << ip << "\n";
    std::cout << "Target PIN: " << pin << "\n";

    ps3rp::Client client;
    
    if (!client.init()) {
        std::cerr << "Failed to initialize PS3RP Client\n";
        return 1;
    }

    std::cout << "Client initialized. Connecting...\n";
    
    if (!client.connect(ip, pin)) {
        std::cerr << "Failed to connect or authenticate to PS3\n";
        return 1;
    }

    std::cout << "Connected! Initializing AVDecoder for H264 Video...\n";
    
    ps3rp::AVDecoder decoder(ps3rp::AVDecoder::CodecType::VIDEO_H264);
    if (!decoder.init()) {
        std::cerr << "Warning: Failed to initialize AVDecoder, continuing anyway...\n";
    }

    std::cout << "Entering receive loop (press Ctrl+C to stop)...\n";
    
    std::vector<uint8_t> buffer(65535);
    int empty_reads = 0;

    // Basic loop
    while (true) {
        int bytes = client.receive(buffer.data(), buffer.size());
        
        if (bytes > 0) {
            std::cout << "Received " << bytes << " bytes of data.\n";
            // Optional: feed to decoder
            auto frames = decoder.decode(buffer.data(), bytes);
            if (!frames.empty()) {
                std::cout << "Decoded " << frames.size() << " frames!\n";
                for (auto f : frames) {
                    av_frame_free(&f);
                }
            }
            empty_reads = 0;
        } else if (bytes < 0) {
            std::cerr << "Error receiving data. Connection closed?\n";
            break;
        } else {
            // bytes == 0
            empty_reads++;
            if (empty_reads > 50) {
                // don't spin indefinitely
                std::this_thread::sleep_for(std::chrono::milliseconds(10));
            }
        }
    }

    return 0;
}