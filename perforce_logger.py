import os
import subprocess
import time
from discord_webhooks import DiscordWebhooks
from settings import DISCORD_WEBHOOK_URL


class PerforceLogger():
    def __init__(self):
      """ Initializes a 30 second timer used to check if commits have been made.  """
      self.global_store = {
        'latest_change': ''
      }

      timer = time.time()

      while True:
        self.post_changes()
        time.sleep(30.0 - ((time.time() - timer) % 30.0))

    def check_p4(self):
      """ Runs the p4 changes command to get the latest commits from the server. """
      p4_changes = subprocess.Popen('p4 changes -t -m 1 -l', stdout=subprocess.PIPE, shell=True)
      return p4_changes.stdout.read().decode('ISO-8859-1')

    def check_for_changes(self):
      """ Figures out if the latest p4 change is new or should be thrown out. """
      output = self.check_p4()

      if output != self.global_store['latest_change']:
        self.global_store['latest_change'] = output

        if '*pending*' in output: 
          return ''

        else:
          return output

      else: 
        return ''

    def post_changes(self):
      """ Posts the changes to the Discord server via a webhook.  """
      payload = self.check_for_changes()

      if payload != '':
        message = DiscordWebhooks(DISCORD_WEBHOOK_URL)
        message.set_content(color=0xc8702a, description='`%s`' % (payload))
        message.set_author(name='Perforce')
        message.set_footer(text='https://github.com/JamesIves/perforce-commit-discord-bot', ts=True)
        message.send()

      else:
        return
