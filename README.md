# # Romeo # (Romeov1) # (MadBoy)
## An exclusive Group Moderator Bot.... 
### Can be found as @Romeo1Bot on Telegram, or [ROMEO](https://telegram.me/Romeo1Bot).

<p align="center">
  <img src="https://telegra.ph/file/f96a2b34ddecce4ad1417.jpg">
</p>

# Romeov3

<p align="center">
- x -|│  “	Superb Group Moderator... ”  │| - x -
</p>

<<p align="center">
<a href="https://app.codacy.com/gh/madboy482/Romeo?utm_source=github.com&utm_medium=referral&utm_content=madboy482/Romeo&utm_campaign=Badge_Grade_Settings" alt="Codacy Badge">
<img src="https://api.codacy.com/project/badge/Grade/6141417ceaf84545bab6bd671503df51" /> </a>
<a href="https://github.com/madboy482/Romeo" alt="Libraries.io dependency status for GitHub repo"> <img src="https://img.shields.io/librariesio/github/madboy482/Romeo" /> </a>
<a href="http://hits.dwyl.com/madboy482/Romeo" alt="HitCount"> <img src="http://hits.dwyl.com/madboy482/Romeo.svg" /> </a>
</p>
<p align="center">
<a href="https://github.com/madboy482/Romeo" alt="GitHub closed issues"> <img src="https://img.shields.io/github/issues-closed-raw/madboy482/Romeo?style=flat&logo=github&color=success" /> </a>
<a href="https://github.com/madboy482/Romeo" alt="GitHub commit activity"> <img src="https://img.shields.io/github/commit-activity/m/madboy482/Romeo" /> </a>
<a href="https://github.com/madboy482/Romeo/network/members" alt="GitHub forks"> <img src="https://img.shields.io/github/forks/madboy482/Romeo?label=Forks&logo=github" /> </a>
<a href="https://github.com/madboy482/Romeo" alt="GitHub closed pull requests"> <img src="https://img.shields.io/github/issues-pr-closed-raw/madboy482/Romeo?color=success" /> </a>
<a href="https://github.com/madboy482/Romeo" alt="GitHub issues"> <img src="https://img.shields.io/github/issues-raw/madboy482/Romeo?style=flat&logo=github&color=yellow" /> </a>
</p>
<p align="center">
<a href="https://github.com/madboy482/Romeo" alt="GitHub release (latest by date including pre-releases)"> <img src="https://img.shields.io/github/v/release/madboy482/Romeo?include_prereleases?style=flat&logo=github" /> </a>
<a href="https://www.python.org/" alt="made-with-python"> <img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg?style=flat&logo=python&color=blue" /> </a>
<a href="https://github.com/madboy482/Romeo" alt="Docker!"> <img src="https://aleen42.github.io/badges/src/docker.svg" /> </a>
<a href="https://github.com/madboy482/Romeo" alt="GitHub repo size"> <img src="https://img.shields.io/github/repo-size/madboy482/Romeo" /> </a>
<a href="https://github.com/madboy482/Romeo/blob/master/LICENSE" alt="GPLv3 license"> <img src="https://img.shields.io/badge/License-GPLv3-blue.svg" /> </a>
</p>
<p align="center">
<a href="https://telegram.me/Romeo_JulietBotSupport" alt="Telegram!"> <img src="https://aleen42.github.io/badges/src/telegram.svg" /> </a>
<a href="https://github.com/madboy482/Romeo/graphs/commit-activity" alt="Maintenance"> <img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" /> </a>
<a href="https://makeapullrequest.com" alt="PRs Welcome"> <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" /> </a>
</p>
  
## ROMEO-3.0 IS A SUPERB GROUP MODERATOR BOT FOR TELEGRAM GROUPS, IT HELPS ADMINS/OWNERS TO MANAGE THEIR GROUPS EASILY.....

# ABOUT

* Bot Link:  <a href="https://telegram.me/Romeo1Bot" alt="Romeo-3.0"> <img src="https://img.shields.io/badge/%F0%9F%A4%96%20-ROMEOv1-blue" /> </a>
* Updates channel: <a  href="https://telegram.me/Romeo_JulietBotSupport" alt="Romeo_JulietBotSupport"> <img  src="https://img.shields.io/badge/%F0%9F%92%A1-ROMEOv3%20Bot%20Support-9cf" /> </a>

* Should you be forking this repo then do not forget to star it - <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/madboy482/Romeo?color=white&label=%F0%9F%8C%9F%20star">

<details>
  <summary># Steps to deploy on Heroku!! </summary>

```
Fill in all the details, Deploy!
Now go to https://dashboard.heroku.com/apps/(app-name)/resources ( Replace (app-name) with your app name )
REMEMBER: Turn on worker dyno (Don't worry It's free :D) & Webhook
Now send the bot /start, If it doesn't respond go to https://dashboard.heroku.com/apps/(app-name)/settings and remove webhook and port.
```

  [![Deploy Here](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/madboy482/Romeo.git)

</details>  



<details>
  <summary># Steps to self Host!! </summary>

  ## Setting up the Bot (Read this before trying to use!):
Please make sure to use python3.6, as I cannot guarantee everything will work as expected on older Python versions!
This is because markdown parsing is done by iterating through a dict, which is ordered by default in 3.6.

  ### Configuration

There are two possible ways of configuring your bot: a config.py file, or ENV variables.

The preferred version is to use a `config.py` file, as it makes it easier to see all your settings grouped together.
This file should be placed in your `SaitamaRobot` folder, alongside the `__main__.py` file. 
This is where your bot token will be loaded from, as well as your database URI (if you're using a database), and most of
your other settings.

It is recommended to import sample_config and extend the Config class, as this will ensure your config contains all
defaults set in the sample_config, hence making it easier to upgrade.

An example for `config.py` file could be:
```
from SaitamaRobot.sample_config import Config

class Development(Config):
    OWNER_ID = 1078841825  # your telegram ID
    OWNER_USERNAME = "Warning_MadBoy_is_Here"  # your telegram username
    API_KEY = "your bot api key"  # your api key, as provided by the @botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/database'  # sample db credentials
    JOIN_LOGGER = '-1234567890' # some group chat that your bot is a member of
    USE_JOIN_LOGGER = True
    DRAGONS = [1107922726]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
```

If you can't have a config.py file (Ex - on Heroku), it is also possible to use environment variables.
So just go and read the config sample file. 
</details>


## Setup on Heroku 
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/madboy482/Romeo.git) 


# Credits 📍
## ➥ <b>OWNER</b> » <a href="https://github.com/madboy482" alt="MadBoy"> <img src="https://img.shields.io/badge/MADBOY-30302f?logo=github" /></a> or <a href="https://telegram.me/Warning_MadBoy_is_Here" alt="MadBoy"> <img src="https://img.shields.io/badge/MADBOY-dcdcdc?logo=telegram" /></a>

## ➥ <b>DEV</b> » <a href="https://telegram.me/Wanacoins" alt="Pranav"> <img src="https://img.shields.io/badge/PRANAV-adff2f?logo=telegram" /></a>
