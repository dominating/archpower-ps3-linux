# CFW PS3 Remote Play Protocol Flow

Based on the reference implementation in `open-rp`, the Remote Play protocol for the PS3 uses standard HTTP/1.1 requests for setup, control, streaming, and input, secured with AES CBC encryption and custom `PREMO-Auth` headers.

## Endpoints

Base URL: `http://<PS3_IP>:<PORT>`
Default Port: Typically `9293` (needs verification from config)
User-Agent: `premo/1.0.0 libhttp/1.0.0`

### 1. Handshake & Session Initialization
**Endpoint:** `GET /sce/premo/session`

- **Headers Required:**
  - `Accept: */*;q=0.01`
  - `PREMO-Auth: <Base64_Encoded_Key>` (derived from `auth_normal` key config)
  - `Connection: Keep-Alive`
- **Behavior:** 
  - Establishes the session ID.
  - Returns headers containing stream codecs and configurations.
  - Generates the base AES keys from the `xor_pkey` bitwise operation.

### 2. Control / Bitrate Selection
**Endpoint:** `GET /sce/premo/session/ctrl`

- **Behavior:** 
  - Allows the client to request bitrate changes (e.g., 256kbps, 384kbps, 512kbps, 768kbps).
  - Uses `PREMO-Auth` derived from `auth_change_bitrate` key config.

### 3. Video Stream
**Endpoint:** `GET /sce/premo/session/video`

- **Behavior:**
  - Opens a persistent HTTP stream.
  - The stream returns chunked packet structures.
  - **Decryption:** Video packets (H.264 / MPEG4) are AES CBC encrypted. The AES Initial Vector (IV) is set to the `xor_nonce` for *each packet*.
  - Decryption key is derived from `AES_set_decrypt_key(videoConfig->key.xor_pkey)`.

### 4. Audio Stream
**Endpoint:** `GET /sce/premo/session/audio`

- **Behavior:**
  - Opens a persistent HTTP stream similar to Video.
  - **Decryption:** Audio packets (AAC / ATRAC3) follow the same AES CBC encryption rules, resetting the IV to `xor_nonce` per packet.

### 5. Controller Input (Pad State)
**Endpoint:** `POST /sce/premo/session/pad`

- **Behavior:**
  - Pushes raw byte structures representing PS3/PSP controller states.
  - Includes events for button press (`KEYDOWN: 0x20000000`), button release (`KEYUP: 0x10000000`), and analog stick axes.
  - Requires timestamp and event ID tracking to keep inputs synced.

## Packet Structure
Each chunked frame from the AV streams contains an `orpStreamPacketHeader_t` indicating the payload length, timestamps, and a magic identifier (`0xff`, `0x80`, etc.) to distinguish video keyframes from audio blocks.

---
*Status: Extracted from `open-rp/orp.cpp` and `open-rp/orp.h`. Ready for C/C++ Chiaki-NG HTTP porting.*