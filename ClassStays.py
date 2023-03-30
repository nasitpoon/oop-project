class Stays:
    def __init__(self, name, type, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description):
        self._name = name
        self._type = type
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
        # self._number_of_room = number_of_room
        self._contact = "48 Oriental Avenue, Bangkok 10500, Thailand +66 (0) 2 659 9000 mobkk-reservations@mohg.com"

    
    def get_name(self):
        return self._name

    def get_type(self):
        return self._type

    def get_room_number(self):
        return self._room_number

    def get_bed_type(self):
        return self._bed_type

    def get_size(self):
        return self._size

    def get_toilet_type(self):
        return self._toilet_type

    def get_complimentary(self):
        return self._complimentary

    def get_speaker(self):
        return self._speaker

    def get_coffee_machine(self):
        return self._coffee_machine

    def get_bathrobes(self):
        return self._bathrobes

    def get_details(self):
        return self._details

    def get_highlights(self):
        return self._highlights

    def get_description(self):
        return self._description


class Rooms(Stays):
    def __init__(self, name, type, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description):
        Stays.__init__(self, name, type, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description)
        self._reserved_room = []

    def __str__(self):
        return self._name + '\n' + self._description
    
    def selected_room(room, suite):
        pass

class Suites(Stays):
    def __init__(self, name, type, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description):
        Stays.__init__(self, name, type, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description)
        self._reserved_room = []
    pass