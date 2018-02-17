# Perforce Commit Logger Discord Bot
This is a small [Discord](https://discordapp.com/) bot that pushes commits made on a [Perforce version control](https://www.perforce.com/) server to a Discord channel. I initially created this for [Red Moon Workshop](https://redmoonworkshop.net/) as there's no webhooks for the free version of Perforce, and they wanted a way to track their developers progress without running a terminal command.

## Requirements
This application requires [Python 3.6.1](https://www.python.org/) and the following packages which can be installed with pip.

```
requests==2.13.0
```

It also requires the [dhooks module by kyb3r](https://github.com/kyb3r/dhooks) which has been included in the repository.

## How It Works
Every thirty seconds the bot runs a Perforce command in the terminal that checks for the most recent changes. If it finds one it stores it, if the change it finds is the same as the one it gathered previously then it discards it. You'll need to provide the bot with access to your servers Perforce command line. One way of doing this is running the Python application on the server which hosts your Perforce server. If you can type `p4 changes` yourself then the bot will be able to do its thing.


## Configuration
In order to power this bot you'll require a [Discord Webhook URL]((https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks)) which you can find within the settings menu for a specific channel. The URL should be stored as an environment variable.

| Key  | Value Information |
| ------------- | ------------- |
| `DISCORD_WEBHOOK_URL`  | The [Webhook URL](https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks) for the Discord channel you'd like the bot to post its messages to. |


## Starting the Bot 
Once you've configured the bot, run `$ python app.py` in the terminal and the bot should begin posting the Perfoce servers commit logs to the channel.

![Example](assets/readme.png)
