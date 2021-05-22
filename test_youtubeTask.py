import unittest
from youtubeTask import *
from itertools import chain, repeat


class TestGetPlaylistID(unittest.TestCase):
    # Test get_playlist_id function with proper playlist link
    def test_get_playlist_id_with_playlist_link(self):
        expression = get_playlist_id(
            'www.youtube.com/watch?v=g4Fny0Zz5j8&list=PLkcctaU57y5ctgdK18QBThxJ8G4mB9q-u')
        expectedValue = 'PLkcctaU57y5ctgdK18QBThxJ8G4mB9q-u'
        failMessage = 'Test Failed : get_playlist_id function with proper playlist link'

        self.assertEqual(expression, expectedValue, failMessage)

    # Test get_playlist_id function with link of a video in a playlist
    def test_get_playlist_id_with_video_link_of_playlist(self):
        expression = get_playlist_id(
            'https://www.youtube.com/watch?v=h3XQMEuwiY0&list=PL-lwbotZANgSkUIqPvpeGM-0btPe9EJPC&index=3&ab_channel=HenryCodingstack')
        expectedValue = 'PL-lwbotZANgSkUIqPvpeGM-0btPe9EJPC'
        failMessage = 'Test Failed : get_playlist_id function with link of a video in a playlist'

        self.assertEqual(expression, expectedValue, failMessage)

    # Test get_playlist_id function with link of not a playlist
    def test_get_playlist_id_with_link_of_not_a_playlist(self):
        expression = get_playlist_id(
            'https://www.youtube.com/watch?v=h3XQMEuwiY0&index=3&ab_channel=HenryCodingstack')
        expectedValue = None
        failMessage = 'Test Failed : get_playlist_id function with link of not a playlist'

        self.assertEqual(expression, expectedValue, failMessage)


class TestHumanReadableTime(unittest.TestCase):
    # Test human_readable_time function for only seconds
    def test_human_readable_time_only_seconds(self):
        expression = human_readable_time(50)
        expectedValue = '50 secs'
        failMessage = 'Test Failed : human_readable_time function for only seconds'

        self.assertEqual(expression, expectedValue, failMessage)


if __name__ == '__main__':

    suite = None
    print('Choose which functions to test :')
    prompts = chain(['1 : get_playlist_id\n2 : human_readable_time\nall : Choose all test\n'], repeat(
        "Wrong option! Try again : ", 2))
    replies = map(input, prompts)

    valid_response = next(filter(lambda option: option in [
        '1',
        '2',
        '3',
        'all'
    ], replies), None)

    if valid_response:
        if valid_response == '1':
            suite = unittest.TestSuite(
                (unittest.makeSuite(TestGetPlaylistID),))

        elif valid_response == '2':
            suite = unittest.TestSuite(
                (unittest.makeSuite(TestHumanReadableTime),))

        elif valid_response == 'all':
            listOfTests = [
                TestGetPlaylistID,
                TestHumanReadableTime
            ]

            initiatedListOfTests = map(
                lambda test: unittest.makeSuite(test), listOfTests)
            suite = unittest.TestSuite(initiatedListOfTests)

        # Run test cases
        result = unittest.TextTestRunner(verbosity=2).run(suite)
    else:
        print('Max tries over!')
        exit()
