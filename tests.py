import unittest
from unittest import mock
import json
from perforce_logger import PerforceLogger

class BaseTest(unittest.TestCase):


  def test_check_for_changes(self):
    PerforceLogger.check_p4 = mock.Mock(return_value="mocked stuff")

    self.assertEqual(PerforceLogger.check_for_changes(), 'This is the return value')

if __name__ == '__main__':
    unittest.main()