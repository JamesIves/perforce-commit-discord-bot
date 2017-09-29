import os
import subprocess
import discord
import asyncio
import time

from settings import *

client = discord.Client()

global_store = {
  'latest_change': ''
}

def check_for_changes():
  p4_changes = subprocess.Popen('p4 changes -t -m 1', stdout=subprocess.PIPE, shell=True)
  output = p4_changes.stdout.read().decode("utf-8")
  print('checking')
  print(output)
  if output != global_store['latest_change']:
    #lets print the chnage
    print('they are not the same')
    global_store['latest_change'] = output

    return output

  else: 
    print('they match, disregard')
    return ''

@client.event
async def post_changes():
  print('posting changes')
  payload = check_for_changes()

  if payload != '':
    await client.send_message(discord.Object(id='276383733945204736'), '`%s`' % (payload))

  else:
    return

@client.event
async def on_ready():
  t=time.time()
  while True:
    await post_changes()
    await asyncio.sleep(30)

client.run(DISCORD_BOT_TOKEN)