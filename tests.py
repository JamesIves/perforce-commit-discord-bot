import unittest
import json
from app import PerforceLogger

class BaseTest(unittest.TestCase):

  def test_check_for_changes_save(self):
    logger = PerforceLogger('webhook_url')

    # Initial change check should save the payload.
    logger.check_for_changes('Change num on date hh:mm:ss by user@client [status] description')
    self.assertEqual(logger.global_store['latest_change'], 'Change num on date hh:mm:ss by user@client [status] description')

    # Additional updates should change the store.
    logger.check_for_changes('Payload should change')
    self.assertEqual(logger.global_store['latest_change'], 'Payload should change')


  def test_check_for_changes_return(self):
    logger = PerforceLogger('webhook_url')

    self.assertEqual(logger.check_for_changes('Payload should return'), 'Payload should return')
    # The payload should return empty as it's the same change as the previous one.
    self.assertEqual(logger.check_for_changes('Payload should return'), '')

    # Should properly throw out **pending** payloads.
    self.assertEqual(logger.check_for_changes('Payload should return empty as its **pending**'), '')
    self.assertEqual(logger.check_for_changes('Payload should return data as its **new**'), 'Payload should return data as its **new**')

if __name__ == '__main__':
    unittest.main()