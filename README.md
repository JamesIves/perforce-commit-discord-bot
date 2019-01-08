# Perforce Commit Logger Discord Bot 🗒️ ✏️

[![Build Status](https://travis-ci.org/JamesIves/perforce-commit-discord-bot.svg?branch=master)](https://travis-ci.org/JamesIves/perforce-commit-discord-bot) [![Issues](https://img.shields.io/github/issues/JamesIves/perforce-commit-discord-bot.svg)](https://github.com/JamesIves/perforce-commit-discord-bot/issues)

With this bot you're able to keep track of commits made to a [Perforce version control](https://www.perforce.com/) server within a [Discord](https://discordapp.com/) channel. 

## Installation Steps 💽

1. Within your Discord server go to the settings for the channel you'd like the commit logs to be posted to and copy the webhook URL.
2. Save the webhook URL as an environment variable called `DISCORD_WEBHOOK_URL`. 
3. The service requires access to the `p4 changes` command in the terminal, your bot should be installed somewhere where it can automatically perform this command without the session expiring. Once suitable access has been provided you'll need to run `$ pip install -r requirements.txt` followed by `$ python app.py` to initialize it.
4. Optionally you should consider creating a CRON script or something similar that restarts the `app.py` file on server reboot in order to keep the bot alive.

---

Unit tests can be run using the `$ python tests.py` command.

## Getting Started :airplane:

Every thirty seconds the bot runs a Perforce command in the terminal that checks for the most recent changes. If it finds one it stores it in memory, if the change it finds is the same as the one it gathered previously then it discards it. You'll need to provide the bot with access to your servers Perforce command line. One way of doing this is running the Python application on the server which hosts your Perforce instance. If you can type `p4 changes` yourself then the bot will be able to do its thing.

## Configuration 📁

The installation will require you to enter a number of settings as environment variables. Below you'll find an explanation of each.

| Key  | Value Information | Required |
| ------------- | ------------- | ------------- |
| `DISCORD_WEBHOOK_URL`  | The [Webhook URL](https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks) for the Discord channel you'd like the bot to post its messages to. | **Yes** |


![Example](assets/readme.png)
