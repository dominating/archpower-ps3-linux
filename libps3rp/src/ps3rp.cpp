#include "ps3rp.h"
#include <iostream>

namespace ps3rp {

Client::Client() {}
Client::~Client() {}

bool Client::init() {
    std::cout << "PS3RP Client Init" << std::endl;
    return true;
}

bool Client::connect(const std::string& ip, const std::string& pin) {
    std::cout << "PS3RP Client Connect: " << ip << std::endl;
    return true;
}

int Client::receive(uint8_t* buffer, int max_size) {
    return 0;
}

} // namespace ps3rp
