class Song:
    def __init__(self, name):
        self.name = name

class Guest:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash

    def __repr__(self):
        return f"Guest('{self.name}', {self.cash})"
    
    def can_afford(self, amount):
        return self.cash >= amount
    
    def deduct_cash(self, amount):
        if self.can_afford(amount):
            self.cash -= amount

class Room:
    def __init__(self, capacity, entry_fee):
        self.playlist = []
        self.guests = []
        self.capacity = capacity
        self.entry_fee = entry_fee

    def add_song(self, song):
        self.playlist.append(song)

    def add_guest(self, guest):
        if len(self.guests) < self.capacity \
        and guest.can_afford(self.entry_fee):
            self.guests.append(guest)
            guest.deduct_cash(self.entry_fee)

    def remove_guest(self, guest):
        if guest in self.guests:
            self.guests.remove(guest)

    