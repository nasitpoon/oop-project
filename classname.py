from enum import Enum
import roominstance as r

class BookingStatus(Enum):
    PENDING, CONFIRMED, CANCELLED = 1, 2, 3
    

class RoomStatus(Enum):
    AVAILABLE, UNAVAILBLE = 1, 2


class PaymentStatus(Enum):
    UNPAID, PENDING, COMPLETE, CANCELLED, REFUNDED = 1, 2, 3, 4, 5


class Stays:
    def __init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description):
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
        # self._number_of_room = number_of_room
        self._contact = "48 Oriental Avenue, Bangkok 10500, Thailand +66 (0) 2 659 9000 mobkk-reservations@mohg.com"
    
    def _showdata(self):
        print(self._name)
        print(self._contact)
        


class Rooms(Stays):
    def __init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description):
        Stays.__init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description)
        self._reserved_room = []

    def __str__(self):
        return self._name + '\n' + self._description
    
    def selected_room(room, suite):
        pass

class Suites(Stays):
    def __init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description):
        Stays.__init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description)
        self._reserved_room = []
    pass



# print(room_Madarin)
#show data
# Stays._showdata(room_Chaophraya)
#print(vars(room_Chaophraya))

class RoomCatalog:
    def __init__(self, name=1, room_number=1, bed_type=1, size=1, toilet_type=1, complimentary=1, speaker=1, coffee_machine=1, bathrobes=1, details=1, highlights=1, description=1, room_count=1, contact=1):
        Stays.__init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description)
        self.catalog_dict = {"Stays" : [
                                            r.room_Chaophraya, r.room_Madarin, r.room_Deluxepremier, r.room_Deluxebalcony, r.room_State, r.room_Siam1bedroomSuite, r.room_Ambassador2bedroomSuite,
                                            r.room_RoyalSuite, r.room_AuthorsSuite, r.room_ChaophrayaSuite, r.room_Deluxe1bedroomthemeSuite, r.room_Deluxe2bedroomthemeSuite, r.room_JuniorterraceSuite, 
                                            r.room_ChaophrayaSuite, r.room_Deluxe1bedroomSuite, r.room_Deluxe2bedroomSuite, r.room_Siam1bedroomSuite, r.room_Selandia2bedroomSuite, r.room_Oriental2bedroomSuite
                                          ],
                                "Rooms" : [ 
                                            r.room_Chaophraya, r.room_Madarin, r.room_Deluxepremier, r.room_Deluxebalcony, r.room_State
                                           ],
                                "Suites" : [
                                            r.room_Siam1bedroomSuite, r.room_Ambassador2bedroomSuite,
                                            r.room_RoyalSuite, r.room_AuthorsSuite, r.room_ChaophrayaSuite, r.room_Deluxe1bedroomthemeSuite, r.room_Deluxe2bedroomthemeSuite, r.room_JuniorterraceSuite, 
                                            r.room_ChaophrayaSuite, r.room_Deluxe1bedroomSuite, r.room_Deluxe2bedroomSuite, r.room_Siam1bedroomSuite, r.room_Selandia2bedroomSuite, r.room_Oriental2bedroomSuite
                                            ]
                               }
        self.room_list_name = []
        self.room_list_description = []
    
    def user_select(self, type):
        # print(self.catalog_dict["Rooms"][2]._description)
        for key,value in self.catalog_dict.items():
            if type == key:
                for i in range(len(value)):
                    self.room_list_name.append(str(value[i]._name))
                    self.room_list_description.append(str(value[i]._description))
                return self.room_list_name,self.room_list_description
        #     # else:
        #     #     raise Exception("Invalid Input")
            
    
    def select_room(self, room_name):
        l = self.catalog_dict[self.room_list].values()
        for value in l:
            if room_name == value:
                return value
            else:
                raise Exception("Invalid Input")
            
room = RoomCatalog()  
# print("hhh")r
name,description = room.user_select("Rooms")
print(name)
print(description)


            
            
class Contact:
    def __init__(self, header_info, general_enquires, reservation, sales_marketing, dining, weddings, events, spa):
        self.__header_info = header_info
        self.__general_enquires = general_enquires
        self.__reservation = reservation
        self.__sales_marketing = sales_marketing
        self.__dining = dining
        self.__weddings = weddings
        self.__events = events
        self.__spa = spa
    pass


class Payment:
    def __init__(self, first_name, last_name, email, email_confirmation, country, phone_number, street_address, city, state_province, postal_code,date_of_birth, additional_info, terms_conditions, unpaid):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._email_confirmation = email_confirmation
        self._country = country
        self._phone_number = phone_number
        self._street_address = street_address
        self._city = city
        self._state_province = state_province
        self._postal_code = postal_code
        self._date_of_birth = date_of_birth
        self._additional_info = additional_info
        self._terms_conditions = terms_conditions
        self._unpaid = unpaid
    
    def insert_card():
        pass


class Booking:
    def __init__(self, calendar, check_in, check_out, room_price, total_price, currency):
        self.__calendar = calendar
        self.__check_in = check_in
        self.__check_out = check_out
        self.__room_price = room_price
        self.__total_price = total_price
        self.__currency = currency
    def booked_info():
        pass


class CreditPayment:
    def __init__(self, card_number, cardholder_name, expiration_date):
        self.__card_number = card_number
        self.__cardholder_name = cardholder_name
        self.__expiration_date = expiration_date
    pass


class SpecialCode:
    def __init__(self, iata_number, promo_code, group_code):
        self.__iata_number = iata_number
        self.__promo_code = promo_code
        self.__group_code = group_code
    pass


class Hotel:
    def __init__(self, name, branch, location):
        self.__name = name
        self.__branch = branch
        self.__location = location
    pass


class User:
    def __init__(self, email, password, status):
        self._email = email
        self._password = password
        self._status = status

    def watch_rooms():
        pass


class Member(User):
    def __init__(self, email, password, status, member_id):
        User.__init__(self, email, password, status)
        self.__member_id = member_id
    
    def selet_room(start_date, end_date):
        pass

    def watch_rooms():
        pass

    def user_info():
        pass

    def has_code():
        pass

class Guest(User):
    def __init__(self, email, password, status):
        User.__init__(self, email, password, status)
    pass


class Admin(User):
    def __init__(self, email, password, status):
        User.__init__(self, email, password, status)
    pass


class BookingHistory:
    def __init__(self, room_number, date, nights):
        self.__room_number = room_number
        self.__date = date
        self.__nights = nights

class SelectedRoom:
    pass

class CreditCard:
    def __init(self):
        pass

    def card_info():
        pass

class PaymentInfo:
    pass

class ManageBooking:
    pass

class BookStays:
    def __init__(self):
        pass
    def create_booking(option):
        pass

#new