# SalmonRun Tweet Bot
Salmon run reminder: Tweets salmon run schedule

## Feature
- Search tweets by hash-tag and re-tweet them
- Get schedules from Splatoon wiki
- (Disable) Repeat crawl and post until success when the internet connection is unstable
- Post Salmon run schedule and it's image

## TODO
- OAuth Nintendo(pending)
  - Maybe this is illegal.
- Code rearrange(delete legacy code)
- Tools for designer
- Change method of import private keys

# Discord Chatting room Bot

## Features
- Post url of latest salmon run tweet
- Post meme url
- Select various options
- Random weapons

## TODO
- refactoring with test code
- based on DNLab Discord Bot
- change parsing rule
- salmonrun schedule parsing rules

# Install(Usage)
- set Google Spreadsheet API to \*.json
- set Twitter API to tweet\_key.py
- download stage and weapon images to images/
  - only use higher 256px images, if not you get error
- download font.ttf to fonts/
  - need English and Japanese font
- submodule update --init --remote

# Created by(Main contributor)
- lapiren
- LunaticHarmony(munhyunsu@gmail.com)
