# PS3 Homebrew Revival & Modding Projects

## Core Objectives
1. **Finish Stalled Homebrew Games**
   - **Super Mario War (PS3 Port):** Update the existing outdated port with modern controller bindings, widescreen support, and implement a custom netcode layer for online multiplayer.

2. **Recreate Canceled Titles**
   - **Eight Days:** Rebuild prototype tech demos utilizing leaked animation and environment assets within an open-source PS3-compatible engine.
   - **TimeSplitters 4:** Recreate early leaked levels and mechanics, porting the assets into a homebrew engine to give the community a playable "what if" slice.

## Tech Stack
- **SDK:** PSL1GHT (Open-source PS3 toolchain) / unofficial SDKs
- **Graphics:** RSXGL / Tiny3D (hardware accelerated graphics for homebrew)
- **Netcode:** libnet / custom UDP rollback layer for Super Mario War
- **Asset Pipeline:** Blender scripts to convert leaked PS2/PS3 assets to homebrew-friendly formats (obj, gltf, custom binary).