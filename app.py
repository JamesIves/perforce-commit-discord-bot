import os
import subprocess
import discord
import asyncio

from settings import *

client = discord.Client()

# Stores the most recent commit.
global_store = {
  'latest_change': ''
}

def check_for_changes():
  """ Runs the p4 changes command to get the latest commits from the server. """
  p4_changes = subprocess.Popen('p4 changes -t -m 1', stdout=subprocess.PIPE, shell=True)
  output = p4_changes.stdout.read().decode("utf-8")

  if output != global_store['latest_change']:
    global_store['latest_change'] = output

    return output

  else: 
    return ''

@client.event
async def post_changes():
  """ Posts the changes to the server  """
  payload = check_for_changes()

  if payload != '':
    await client.send_message(discord.Object(id='%s') % (DISCORD_CHANNEL_ID), '`%s`' % (payload))

  else:
    return

@client.event
async def on_ready():
  while True:
    await post_changes()
    await asyncio.sleep(30)

client.run(DISCORD_BOT_TOKEN)