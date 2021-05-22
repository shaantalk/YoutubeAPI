import unittest
from test.test_get_playlist_id import *
from test.test_human_readable_time import *


if __name__ == '__main__':
    listOfTests = [
        TestGetPlaylistID,
        TestHumanReadableTime
    ]

    initiatedListOfTests = map(
        lambda test: unittest.makeSuite(test), listOfTests)
    suite = unittest.TestSuite(initiatedListOfTests)

    # Run test cases
    result = unittest.TextTestRunner(verbosity=2).run(suite)
