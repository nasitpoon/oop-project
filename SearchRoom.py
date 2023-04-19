import Roominstance
from DateCal import DateCal
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
        
    def get_rooms_list(self):
        return self.rooms_list
    

class total_cost:
    def __init__(self, start_date, end_date, room_type, room_catalog):
        self.__room_type = room_type
        self.__start_date = start_date
        self.__end_date = end_date
        self.__nights = DateCal().date_diff(start_date, end_date)
        self.__room_price = self.get_price(room_catalog)
        self.__total_cost = self.__room_price * self.__nights

    def get_price(self, room_catalog):
        for room in room_catalog.get_rooms_list():
            if room.get_name() == self.__room_type:
                return room.get_price()      
        raise ValueError(f"No room found for type '{self.__room_name}'")


    def get_total_cost(self):
        return self.__total_cost
    
    def get_start_date(self):
        return self.__start_date
    
    def get_end_date(self):
        return self.__end_date
    
    def get_nights(self):
        return self.__nights
    
    def get_room_type(self):
        return self.__room_type
    
    def get_room_price(self):
        return self.__room_price
    
