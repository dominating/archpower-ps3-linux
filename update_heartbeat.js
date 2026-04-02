const fs = require('fs');
const state = JSON.parse(fs.readFileSync('memory/heartbeat-state.json'));
state.lastChecks.scout = 1774768380;
fs.writeFileSync('memory/heartbeat-state.json', JSON.stringify(state, null, 2));
