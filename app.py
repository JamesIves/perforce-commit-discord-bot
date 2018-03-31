import os
import subprocess
from discord_hooks import Webhook
from settings import DISCORD_WEBHOOK_URL

# Stores the most recent commit.
global_store = {
  'latest_change': ''
}

def check_for_changes():
  """ Runs the p4 changes command to get the latest commits from the server. """
  p4_changes = subprocess.Popen('p4 changes -t -m 1 -l', stdout=subprocess.PIPE, shell=True)
  output = p4_changes.stdout.read().decode('ISO-8859-1')

  if output != global_store['latest_change']:
    global_store['latest_change'] = output

    if '*pending*' in output: 
      return ''

    else:
      return output

  else: 
    return ''

def post_changes():
  """ Posts the changes to the Discord server via a webhook.  """
  payload = check_for_changes()

  if payload != '':
    message = Webhook(DISCORD_WEBHOOK_URL, color=0xc8702a)
    message.set_desc('`%s`' % (payload))
    message.set_footer(text='https://github.com/JamesIves/perforce-commit-discord-bot', ts=True)
    message.post()

  else:
    return

def init():
  """ Initializes a 30 second timer used to check if commits have been made.  """
  import time
  timer = time.time()

  while True:
    post_changes()
    time.sleep(30.0 - ((time.time() - timer) % 30.0))

init()