import unittest
from main import *


class TestHumanReadableTime(unittest.TestCase):
    # Test human_readable_time function for only seconds
    def test_human_readable_time_only_seconds(self):
        expression = human_readable_time(50)
        expectedValue = '50 secs'
        failMessage = 'Test Failed : human_readable_time function for only seconds'

        self.assertEqual(expression, expectedValue, failMessage)

    # Test human_readable_time function for days
    def test_human_readable_time_days(self):
        expression = human_readable_time(8000000)
        expectedValue = '92 days 14 hours 13 mins 20 secs'
        failMessage = 'Test Failed : human_readable_time function for days'

        self.assertEqual(expression, expectedValue, failMessage)
