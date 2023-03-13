import unittest
from src.karaoke import *

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room(4, 10.0)
        self.songs = [
            Song("Ritual Annihilation"),
            Song("Trains"),
            Song("Mamma Mia")
        ]
        self.guests = [
            Guest("Jasper", 20.0),
            Guest("Alex", 20.0),
            Guest("Ed", 20.0),
            Guest("Jack", 20.0),
            Guest("Josh", 20.0)
        ]

    def test_has_playlist(self):
        for song in self.songs:
            self.room.add_song(song)
        self.assertEqual(self.songs, self.room.playlist)

    def test_add_single_guest(self):
        self.room.add_guest(self.guests[0])
        self.assertEqual("Jasper", self.room.guests[0].name)
        self.assertEqual(10.0, self.room.guests[0].cash)

    def test_remove_single_guest(self):
        self.room.add_guest(self.guests[0])
        self.room.remove_guest(self.guests[0])
        self.assertEqual([], self.room.guests)

    def test_remove_only_second_guest(self):
        self.room.add_guest(self.guests[0])
        self.room.add_guest(self.guests[1])
        self.room.remove_guest(self.guests[1])
        self.assertEqual([self.guests[0]], self.room.guests)

    def test_remove_guest_not_found(self):
        self.room.remove_guest(self.guests[0])
        self.assertEqual([], self.room.guests)

    def test_add_guest_max_capacity(self):
        for guest in self.guests:
            self.room.add_guest(guest)
        self.assertEqual(self.guests[:-1], self.room.guests)

    def test_add_guest_insufficient_funds(self):
        poor_guest = Guest("Jasper", 5.0)
        self.room.add_guest(poor_guest)
        self.assertEqual([], self.room.guests)
        self.assertEqual(5.0, poor_guest.cash)