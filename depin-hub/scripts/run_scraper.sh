#!/bin/bash
source ~/venv/bin/activate
cd /home/micemeat/.openclaw/workspace/depin-hub/scripts
python3 update_x_giveaways.py
cd ..
git add index.html
git commit -m "Auto-update X giveaways widget" || exit 0
git push
vercel --prod --yes
