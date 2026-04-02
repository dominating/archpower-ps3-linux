# PRD: Nightly Memory Consolidation and Job Monitoring System

**Goal:** Implement an automated nightly routine to consolidate daily knowledge and monitor long-running job sessions, ensuring continuity and learning for the agent.

**Layers Affected:** Layer 1 (Knowledge Repo), Layer 2 (Daily Notes), Layer 3 (Tacit Knowledge).

## 1. Nightly Memory Consolidation Job (Cron: ~02:00 UTC)
This job runs daily and is responsible for distilling the day's activity into curated, searchable long-term memory.

### 1.1. Memory Consolidation Skill (`consolidate_memory`)
This process must execute daily around 02:00 UTC.

**Inputs:**
- All session transcripts/logs from the current day (Layer 2 context).
- Existing `mice-life/PARA/resources/llm_memories.md` (Layer 1 long-term memory).

**Process:**
1.  **Iterate Daily Logs:** Read all chat sessions associated with the agent for the past 24 hours.
2.  **Extract Key Information:** For each session, extract: Project updates, critical decisions made, resource links, and any new credentials granted.
3.  **Update Layer 2 (Daily Note):** Append extracted summaries to `memory/YYYY-MM-DD.md`.
4.  **Update Layer 1 (Long-term):** Merge significant, non-ephemeral facts/decisions into `mice-life/PARA/resources/llm_memories.md`.
5.  **Rebuild Search Index:** Rebuild the QMD search index to ensure new knowledge is searchable immediately the next day. (Assumes QMD configuration is fixed.)

## 2. Heartbeat Loop Logic Enhancement (Monitoring Running Jobs)
The existing heartbeat mechanism must be updated to monitor sessions associated with "big jobs" delegated to Codeex (ACP sessions).

### 2.1. Job Logging
Whenever a big job starts (e.g., using `sessions_spawn`), log the following in the current day's **Layer 2 Daily Note**:
- Job Name (Label)
- Target Directory (`cwd`)
- Session Key (or Label for tracking)
- Session Type (e.g., ACP Codeex)

### 2.2. Heartbeat Monitoring Task
The nightly cron or heartbeat must check the status of these logged jobs.

**Logic per logged job:**
- **If Session is Running:** Do nothing (allow to complete).
- **If Session Died/Finished Unexpectedly:** Log the failure to the daily note, and attempt a **silent restart** if the job is a known persistent loop (like the latest bot attempt). **Do not spam the user.**
- **If Session Finished Successfully:** Report the completion summary back to the user via a private message (Telegram DM).

## Constraints
- **Path Stability:** Big jobs must run in stable directories (not `/tmp`) so they are not killed by cleanup routines.
- **No Spam:** The system must be passive unless a job fails or completes.
- **Security:** Ensure the nightly consolidation job has appropriate, but restricted, write access only to the memory directories.
