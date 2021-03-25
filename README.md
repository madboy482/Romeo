![Romeo](https://telegra.ph/file/f96a2b34ddecce4ad1417.jpg)

# Romeo

[![Updates channel!](https://img.shields.io/badge/Join%20Channel-!-red)](https://t.me/Romeo_JulietBotSupport)


A modular Telegram Python bot running on python3 with a sqlalchemy database and an entirely themed persona to make Romeo suitable for moderating groups...

Can be found on telegram as [Romeo](https://telegram.me/Romeo1Bot).

The Support group can be reached out to at [Romeo Bot Support](https://t.me/Romeo_JulietBotSupport), where you can ask for help about [Romeo](https://telegram.me/Romeo1Bot), discover/request new features, report bugs, and stay in the loop whenever a new update is available. 

## How to setup/deploy.

<details>
  <summary>Steps to deploy on Heroku !! </summary>

```
Fill in all the details, Deploy!
Now go to https://dashboard.heroku.com/apps/(app-name)/resources ( Replace (app-name) with your app name )
REMEMBER: Turn on worker dyno (Don't worry It's free :D) & Webhook
Now send the bot /start, If it doesn't respond go to https://dashboard.heroku.com/apps/(app-name)/settings and remove webhook and port.
```

  [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/madboy482/Romeo.git)

</details>  
<details>
  <summary>Steps to self Host!! </summary>

  ## Setting up the bot (Read this before trying to use!):
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

An example `config.py` file could be:
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

If you can't have a config.py file (EG on Heroku), it is also possible to use environment variables.
So just go and read the config sample file. 


## How to setup on Heroku 
For starters click on this button 

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/madboy482/Romeo.git) 


# Credits 📍
The bot is based on the original work done by <b>[PaulSonOfLars](https://github.com/PaulSonOfLars)</b>
All original credits go to Paul and his dedication, Without his efforts, this fork would not have been possible!

## ➥ <b>FORK DEVELOPER</b> » <a href="https://github.com/madboy482" alt="MadBoy"> <img src="https://img.shields.io/badge/MADBOY-30302f?logo=github" /></a> or <a href="https://telegram.me/Warning_MadBoy_is_Here" alt="MadBoy"> <img src="https://img.shields.io/badge/MADBOY-dcdcdc?logo=telegram" /></a>

## ➥ <b>DEV</b> » <a href="https://telegram.me/Wanacoins" alt="Pranav"> <img src="https://img.shields.io/badge/PRANAV-adff2f?logo=telegram" /></a>

Also, missing proper credit for blacklistusers taken from TheRealPhoenixBot (will add it later, this note says unless it is done)

Any other authorship/credits can be seen through the commits.

Should any be missing kindly let us know at [Romeo Bot Support](https://t.me/Romeo_JulietBotSupport) or simply submit a pull request on the readme.
