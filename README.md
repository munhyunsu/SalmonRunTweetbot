# SalmonRun Tweet Bot
Salmon run reminder: Tweets salmon run schedule

## Feature
- Search tweets by hash-tag and re-tweet them
- Get schedules from Splatoon wiki
- Post Salmon run schedule and it's image

## TODO
- Image layout
- Refactor
  - Need to re-organize source code
  - Remove modules directory
- Nomalize

# Discord Chatting Bot

## Features
- Inherit DNLab Discord Bot's LuHaBot
- Post url of latest salmon run tweet
- Post meme url
- Random weapons
- Remove non-command chat

## TODO
- refactoring with test code
- need viewer
- salmonrun schedule parsing rules
- Change method of import private keys
- Refactor
  - Need to re-organize source code
  - Remove modules directory
- Change bot command to normal chatbot
  - Need to implement help command
- Yeild loop by minutes

# Install(Usage)
- set Google Spreadsheet API to \*.json
- set Twitter API to tweet\_key.py
- download stage and weapon images to images/
  - only use higher 256px images, if not you get error
- download font.ttf to fonts/
  - need English and Japanese font
- submodule update --init --remote

# White paper
- Need to modulize this project

# Created by(Main contributor)
- lapiren
- LunaticHarmony(munhyunsu@gmail.com)
