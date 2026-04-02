# CFW PS3 Remote Play Project (Chiaki-NG / PSPlay Integration)

## Goal
Implement Remote Play support for Custom Firmware (CFW) PS3 within Chiaki-NG or PSPlay by porting the core logic from `open-rp` to modern platforms.

## Roadmap

### Phase 1: Study & Reference Implementation
- [x] Fork and study `shoobyban/open-rp`
- [ ] Get `open-rp` running on a modern PC/Linux environment to act as a reference implementation.
- [x] Document the protocol flow (handshake, keep-alive, stream init).

### Phase 2: Core Logic Port (C/C++)
- [ ] Port the Authentication layer to C/C++ compatible with Chiaki's architecture.
- [ ] Port HTTP Input processing.
- [ ] Port the Decryption logic.

### Phase 3: Android Renderer (Legacy Codecs)
- [ ] Implement an Android video/audio renderer that handles older codecs utilized by the PS3 Remote Play protocol.
- [ ] Ensure low-latency decoding and syncing.

### Phase 4: Incremental Testing
- [ ] **Test 1:** Connect & Handshake (establish session without crashing).
- [ ] **Test 2:** Input (send controller inputs successfully).
- [ ] **Test 3:** Video/Audio Feed (receive and render the raw AV stream).

### Phase 5: Open-Source Release
- [ ] Prepare the fork for public release on GitHub.
- [ ] Document the build process, known issues, and future goals.
- [ ] Reach out to the community for testing, debugging, and contributions.
