# Perforce Commit Logger Discord Bot
This is a small [Discord](https://discordapp.com/) bot that pushes commits made on a [Perforce version control](https://www.perforce.com/) server to a Discord channel. I initially created this for [Red Moon Workshop](https://redmoonworkshop.net/) as there's no webhooks for the free version of Perforce, and they wanted a way to track their developers progress without running a terminal command.

## Requirements
This application requires [Python 3.6.1](https://www.python.org/) and the following packages which can be installed with pip.

```
discord.py==0.16.7
```

## How It Works
Every thirty seconds the bot runs a Perforce command in the terminal that checks for the most recent changes. If it finds one it stores it, if the change it finds is the same as the one it gathered previously then it discards it. You'll need to provide the bot with access to your servers Perforce command line. One way of doing this is running the Python application on the server which hosts your Perforce server. If you can type `p4 changes` yourself then the bot will be able to do its thing.


## Configuration
In order to power this bot you'll require a [Discord API bot token]((https://discordapp.com/developers/docs/intro)) and a Discord channel ID that you'd like to post the messages to. These credentials are stored as environment variables.

| Key  | Value Information |
| ------------- | ------------- |
| `DISCORD_BOT_TOKEN`  | The token for your Discord bot user, you can sign up for one [here](https://discordapp.com/developers/docs/intro). |
| `DISCORD_CHANNEL_ID`  | The ID of the channel you'd like the bot to post its messages to. You can find this by launching the web version of Discord, joining a channel, and then snipping the long number in the URL path. |


## Inviting the Bot
Once the application is running you'll need to invite the bot to your Discord server. Replace the `YOUR_CLIENT_ID_HERE` portion of the following URL with the one found in your [Discord API settings](https://discordapp.com/developers/docs/intro).

`https://discordapp.com/oauth2/authorize?&client_id=YOUR_CLIENT_ID_HERE&scope=bot&permissions=0`

![Example](assets/example.png)
