# HEARTBEAT.md - Periodic Tasks

## 1. Daily Scout & Media Engine Loop
**Frequency:** Check `memory/heartbeat-state.json` to only execute once every 24 hours.
**Instructions:**
- **Scout:** Use `web_search` to find 2-3 emerging DePIN nodes, airdrop quests, and passive income opportunities.
- **Verification (CRITICAL):** Before proposing *any* project, you MUST read `depin-hub/index.html` to ensure the project is not already listed (e.g., check for alternate names like DePINed, Blockless/Bless, ARO).
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

## 3. Daily Giveaway Scout
**Frequency:** Once daily (can be batched with the Daily Scout).
**Instructions:**
- Use `web_search` to look for new hardware, crypto, or DePIN-related giveaways (e.g., miners like Bitaxe, nodes, hardware wallets).
- If any legitimate active giveaways are found, send a Telegram alert so they can be added to the DePIN Hub giveaways section.





