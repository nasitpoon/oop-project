import uuid
from Booking import Booking
from Register import Account
class User:
    def __init__(self, email, password, status):
        self._email = email
        self._password = password
        self._status = status

    def watch_rooms(self, room_catalog, type):
        return room_catalog.user_select(type)


class Member(User):
    existing_member_ids = set()
    counter = 0

    def __init__(self, fname = '', lname = '', email = '', password = '', phone_number = ''):
        self.__fname = fname
        self.__lname = lname
        self.__status = "ACTIVE"
        self.__email = email
        self.__password = password
        self.__phone_number = phone_number
        self.__member_id = Member.generate_member_id()
        Member.counter += 1
        self.__member_number = Member.counter

    @classmethod
    def generate_member_id(cls):
        while True:
            member_id = str(uuid.uuid4().hex)[:8]
            if member_id not in cls.existing_member_ids:
                cls.existing_member_ids.add(member_id)
                return member_id
        
    def book_room(self, start_date, end_date, room_type):
        return Booking(start_date, end_date, room_type)

    def user_info():
        pass

    def has_code():
        pass

    def get_name(self):
        return self.__fname + " " + self.__lname
    
    def get_phone(self):
        return self.__phone_number
    
    def get_email(self):
        return self.__email
    
    def get_member_id(self):
        return self.__member_id


class Admin(User):
    def __init__(self, email, password, status):
        User.__init__(self, email, password, status)
    
    
    def add_room(self, room_catalog, room):
        room_catalog.add_room(room)

    def update_price(self, room, price):
        room.set_price(price)