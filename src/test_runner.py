import unittest
from tests.test_human_readable_time import *


if __name__ == '__main__':
    listOfTests = [TestHumanReadableTime]

    # Not initiating gives an error
    initiatedListOfTests = map(
        lambda test: unittest.makeSuite(test),
        listOfTests
    )

    suite = unittest.TestSuite(initiatedListOfTests)

    # Run test cases
    result = unittest.TextTestRunner(verbosity=2).run(suite)
