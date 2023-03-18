from enum import Enum

class BookingStatus(Enum):
    PENDING, CONFIRMED, CANCELLED = 1, 2, 3
    

class RoomStatus(Enum):
    AVAILABLE, UNAVAILBLE = 1, 2


class PaymentStatus(Enum):
    UNPAID, PENDING, COMPLETE, CANCELLED, REFUNDED = 1, 2, 3, 4, 5


class Stays:
    def __init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, number_of_room, contact):
        self._name = name
        self._room_number = room_number
        self._bed_type = bed_type
        self._size = size
        self._toilet_type = toilet_type
        self._complimentary = complimentary
        self._speaker = speaker
        self._coffee_machine = coffee_machine
        self._bathrobes = bathrobes
        self._details = details
        self._highlights = highlights
        self._description = description
        self._number_of_room = number_of_room
        self._contact = contact


class Rooms(Stays):
    def __init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, number_of_room, contact):
        Stays.__init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, number_of_room, contact)
        self._reserved_room = []
    pass


class Suites(Stays):
    def __init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, number_of_room, contact, bedroom, connecting, powder_room):
        Stays.__init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, number_of_room, contact)
        self._bedroom = bedroom
        self._connecting = connecting
        self._powder_room = powder_room
        self._reserved_room = []
    pass
