import Roominstance as r

class RoomCatalog:
    def __init__(self):
        self.rooms_list = []
    
    def user_select(self, type):
        if type == "Stays":
            return self.rooms_list
        elif type == "Rooms":
            return_rooms_list = []
            for room in self.rooms_list:
                if room.get_type() == "Room":
                    return_rooms_list.append(room)
            return return_rooms_list
        elif type == "Suites":
            return_rooms_list = []
            for room in self.rooms_list:
                if room.get_type() == "Suite":
                    return_rooms_list.append(room)
            return return_rooms_list
        
    def add_room(self,room):
        self.rooms_list.append(room)

            
room = RoomCatalog()
# name,description = room.user_select("Suites")
# name, description, size, bed_type, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights = room.select_room("Oriental 2-Bedroom Suite")
# print(f"{name}\n{description}\n{size}\n{bed_type}\n{toilet_type}\n{complimentary}\n{speaker}\n{bathrobes}\n{details}\n{highlights}")

room.add_room(r.room_Deluxebalcony)
room.add_room(r.room_AuthorsSuite)

rooms = room.user_select("Rooms")

print(rooms[0].get_name())