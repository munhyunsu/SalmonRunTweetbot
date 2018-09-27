# SalmonRunTweetbot
Salmon run reminder: Tweets salmon run schedule

## Featrues
- Search tweets by hashtag and retweet them
- Get schedules from Splatoon wiki
- (Disable) Repeat crawl and post until success when the internet connection is unstable
- Post Salmon run schedule and it's image

## Install(Usage)
- set Google Spreadsheet API to \*.json
- set Twitter API to tweet\_key.py
- download stage and weapon images to images/
  - only use higher 256px images, if not you get error
- downdload font.ttf to fonts/
  - need english and japenese font
  
## TODO
- OAuth Nintendo(pending)
- Code rearrange(delete legacy code)
- Tools for designer
- Change method of import private keys
- [Bug] Can not write tweet url at Salmon run beginning
  - (Pending) it caused by tweetpy library bug
- Discord bot
  - connect discord server
  - post twitter url

# Created by(Main contributor)
- lapiren
- LunaticHarmony(munhyunsu@gmail.com)
