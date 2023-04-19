class RoomCatalog:
    def __init__(self):
        self.rooms_list = []

    def add_room(self, room):
        self.rooms_list.append(room)

    def user_select(self, type):
        if type == "Stays":
            return self.rooms_list
        elif type == "Rooms":
            temp_rooms_list = [room for room in self.rooms_list if room.get_type() == "Room"]
            return temp_rooms_list
        elif type == "Suites":
            temp_rooms_list = [room for room in self.rooms_list if room.get_type() == "Suite"]
            return temp_rooms_list