#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
#include <cstring>
#include <stdint.h>

// Endianness handling macros (assuming Linux/POSIX or Chiaki-NG's cross-platform macros)
#ifdef _WIN32
#include <winsock2.h>
#else
#include <arpa/inet.h>
#endif

// We need a way to define little-endian swaps.
#if defined(__linux__) || defined(__APPLE__)
#include <endian.h>
#define SWAP_LE16(x) htole16(x)
#else
// Simple fallback for LE swap
static inline uint16_t SWAP_LE16(uint16_t x) {
    uint16_t out;
    uint8_t* p_in = (uint8_t*)&x;
    uint8_t* p_out = (uint8_t*)&out;
    p_out[0] = p_in[0];
    p_out[1] = p_in[1];
    return out;
}
#endif

// External AES definitions (mapping to Chiaki-NG's crypto, e.g., mbedtls or openssl)
#define ORP_KEY_LEN 16

// Dummy AES functions to represent Chiaki's internal crypto abstraction
enum { AES_ENCRYPT, AES_DECRYPT };
struct AES_KEY { uint8_t rd_key[4 * (14 + 1)]; int rounds; };

extern "C" {
void AES_set_decrypt_key(const uint8_t *userKey, const int bits, AES_KEY *key);
void AES_set_encrypt_key(const uint8_t *userKey, const int bits, AES_KEY *key);
void AES_cbc_encrypt(const uint8_t *in, uint8_t *out, size_t length, const AES_KEY *key, uint8_t *ivec, const int enc);
}

struct orpStreamPacketHeader_t {
    uint8_t magic[2];   // 2
    uint16_t frame;     // 4
    uint32_t clock;     // 8
    uint8_t root[4];    // 12
    uint16_t unk2;      // 14
    uint16_t unk3;      // 16
    uint16_t len;       // 18
    uint16_t unk4;      // 20
    uint16_t unk5;      // 22
    uint16_t unk6;      // 24
    uint16_t unk7;      // 26
    uint16_t unk8;      // 28
    uint16_t unk9;      // 30
    uint16_t unk10;     // 32
};

struct orpStreamConfig {
    uint8_t xor_nonce[ORP_KEY_LEN];
    uint8_t xor_pkey[ORP_KEY_LEN];
    AES_KEY aes_key;
    uint8_t iv1[ORP_KEY_LEN];
    std::string name;
};

// Initializes the AES key using the xor_pkey
void InitStreamCrypto(orpStreamConfig& config) {
    AES_set_decrypt_key(config.xor_pkey, ORP_KEY_LEN * 8, &config.aes_key);
}

// Decrypts the raw AV packet payload if it matches the magic bytes
bool DecryptStreamPacket(orpStreamPacketHeader_t* header, uint8_t* payload_data, size_t payload_size, orpStreamConfig& config) {
    bool requires_decryption = false;

    // H.264 Video Key-Frames
    if ((header->magic[1] == 0xff || header->magic[1] == 0xfe) && header->unk6 == SWAP_LE16(0x0401)) {
        requires_decryption = true;
    }
    // AAC Audio
    else if (header->magic[1] == 0x80 && header->unk8) {
        requires_decryption = true;
    }
    // MPEG4 Video Key-Frames
    else if (header->magic[1] == 0xfb && (header->unk6 == SWAP_LE16(0x0001) || header->unk6 == SWAP_LE16(0x0401))) {
        requires_decryption = true;
    }
    // ATRAC3 Audio
    else if (header->magic[1] == 0xfc && header->unk8) {
        requires_decryption = true;
    }

    if (requires_decryption) {
        // IV is reset to the xor_nonce per packet block
        memcpy(config.iv1, config.xor_nonce, ORP_KEY_LEN);
        
        // Decrypt aligning to 16-byte boundaries (ORP_KEY_LEN)
        size_t block_aligned_size = payload_size - (payload_size % ORP_KEY_LEN);
        
        AES_cbc_encrypt(payload_data, payload_data, block_aligned_size, &config.aes_key, config.iv1, AES_DECRYPT);

        // Verification (H.264 video shouldn't start with non-zero byte after decrypt)
        if ((header->magic[1] == 0xff || header->magic[1] == 0xfe) && payload_data[0] != 0x00) {
            std::cerr << "Packet decryption failure. Corrupted video stream." << std::endl;
            return false;
        }
    }

    return true;
}

// PAD State Structure Constants
#define ORP_PADSTATE_LEN 128
#define ORP_PAD_TIMESTAMP 0x40
#define ORP_PAD_EVENTID 0x48

// Encrypts Pad State to push back to PS3
void EncryptPadState(uint8_t* pad_state, uint32_t id, uint32_t timestamp, orpStreamConfig& config) {
    if (id != 0) {
        uint32_t be_id = htonl(id);
        uint32_t be_timestamp = htonl(timestamp);
        memcpy(pad_state + ORP_PAD_EVENTID, &be_id, 4);
        memcpy(pad_state + ORP_PAD_TIMESTAMP, &be_timestamp, 4);
    }

    // Always reset IV for new pad packet
    memcpy(config.iv1, config.xor_nonce, ORP_KEY_LEN);
    
    // Only encrypt if network is public - assume public for standard robust Chiaki client
    AES_KEY encrypt_key;
    AES_set_encrypt_key(config.xor_pkey, ORP_KEY_LEN * 8, &encrypt_key);

    uint8_t pad_crypt[ORP_PADSTATE_LEN];
    memset(pad_crypt, 0, ORP_PADSTATE_LEN);
    
    AES_cbc_encrypt(pad_state, pad_crypt, ORP_PADSTATE_LEN, &encrypt_key, config.iv1, AES_ENCRYPT);

    // Send pad_crypt over HTTP connection...
    // In Chiaki, this will be pushed to the HTTP POST socket pool.
}