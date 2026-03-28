# HEARTBEAT.md - Periodic Tasks

## 1. Daily Scout & Media Engine Loop
**Frequency:** Check `memory/heartbeat-state.json` to only execute once every 24 hours.
**Instructions:**
- **Scout:** Use `web_search` to find 2-3 emerging DePIN nodes, airdrop quests, and passive income opportunities (exclude Grass, Nodepay, Titan, YOM, DataHive, Silencio).
- **Notify:** Send a Telegram message with the scouted projects to get a green light before executing. Wait for user approval.
- **Execute & Deploy:** (Once approved) Write Markdown deep-dives, add them to `depin-hub/index.html`, commit via `git`, and run `vercel --prod --yes`.
- **Self-Evolution Audit:** Analyze workflow efficiency. Search ClawHub for new skills to automate slow tasks (e.g., Discord scrapers). If a new skill is needed, ping the user on Telegram requesting the necessary API access/credentials, and update `skills_log.md`.

## 2. Nightly Memory Consolidation
**Frequency:** Once daily (triggered via nightly cron).
**Instructions:**
- Read yesterday's daily memory file in `memory/`.
- Extract important info, updates, decisions, and resource links.
- Update `MEMORY.md` with long-term curated memories.
- Summarize the consolidation in the daily note.
