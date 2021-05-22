import unittest
from youtubeTask import *


class TestHumanReadableTime(unittest.TestCase):
    # Test human_readable_time function for only seconds
    def test_human_readable_time_only_seconds(self):
        expression = human_readable_time(50)
        expectedValue = '50 secs'
        failMessage = 'Test Failed : human_readable_time function for only seconds'

        self.assertEqual(expression, expectedValue, failMessage)
