import unittest
from src.karaoke import *

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Ritual Annihilation", "Cannibal Corpse")

    def test_has_name(self):
        self.assertEqual("Ritual Annihilation", self.song.name)

    def test_has_artist(self):
        self.assertEqual("Cannibal Corpse", self.song.artist)

    def test___eq__(self):
        self.song2 = Song("Ritual Annihilation", "Cannibal Corpse")
        self.assertTrue(self.song == self.song2)