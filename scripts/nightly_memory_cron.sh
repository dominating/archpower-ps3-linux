#!/bin/bash
# Injects the consolidation task into the agent's heartbeat file at 2 AM
echo "
# ==========================================
# NIGHTLY MEMORY CONSOLIDATION (SYSTEM CRON)
# ==========================================
# Please perform the following tasks immediately:
# 1. Read yesterday's daily memory file in memory/ (e.g., memory/\$(date -d yesterday +%Y-%m-%d).md).
# 2. Extract important info: Project updates, decisions, resource links, and credentials granted.
# 3. Update MEMORY.md (Layer 1) and relevant project pages (Layer 2).
# 4. Rebuild the QMD index / update Markdown references so the knowledge is searchable.
# 5. Append a summary of the consolidation to yesterday's daily note.
# 6. Run git add, commit, and push to the repo.
# 7. Remove this entire nightly consolidation block from HEARTBEAT.md once finished.
" >> /home/micemeat/.openclaw/workspace/HEARTBEAT.md
