#ifndef PS3RP_H
#define PS3RP_H

#include <string>
#include <vector>
#include <cstdint>

namespace ps3rp {

class Client {
public:
    Client();
    ~Client();
    bool init();
    bool connect(const std::string& ip, const std::string& pin);
    int receive(uint8_t* buffer, int max_size);
};

} // namespace ps3rp

#endif // PS3RP_H
