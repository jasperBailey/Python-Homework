import unittest
from src.karaoke import *

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Ritual Annihilation")

    def test_has_name(self):
        self.assertEqual("Ritual Annihilation", self.song.name)