import unittest
import json
import unittest.mock
from unittest.mock import patch
from app import check_for_changes

class BaseTest(unittest.TestCase):


  @mock.patch('subprocess.Popen')
  def test_check_for_changes(self, mock_subproc_popen):
    process_mock = mock.Mock()
    attrs = {'communicate.return_value': 'This is the return value'}
    process_mock.configure_mock(**attrs)
    mock_subproc_popen.return_value = process_mock

    self.assertTrue(mock_subproc_popen.called)
    self.assertEqual(check_p4(), 'This is the return value')

if __name__ == '__main__':
    unittest.main()