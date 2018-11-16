#!/bin/bash

kill -2 $(ps -ef | awk '/[d]iscord_bot.py/ {print $2}')
sleep 5
cd PATH
nohup ./venv/bin/python3 discord_bot.py 2>1 &
