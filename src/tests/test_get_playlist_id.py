import unittest
from youtubeTask import *


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
