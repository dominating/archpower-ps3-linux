const { execSync } = require('child_process');
execSync('npx --yes create-video@latest duino-promo --template blank', {stdio: 'inherit', cwd: './output'});
