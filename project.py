from enum import Enum

class BookingStatus(Enum):
    PENDING, CONFIRMED, CANCELLED = 1, 2, 3
    

class RoomStatus(Enum):
    AVAILABLE, UNAVAILBLE = 1, 2


class PaymentStatus(Enum):
    UNPAID, PENDING, COMPLETE, CANCELLED, REFUNDED = 1, 2, 3, 4, 5


class Stays:
    def __init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, contact):
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
        self._contact = contact
    
    # def all_room():
    #     room1 = {
    #         "name" : "Chao Phraya Room",
    #         "details" : "Located in the Garden Wing, these rooms with either a flat or split-level layout, offer a residential ambience. The rooms are the epitome of classic elegance with a colonial inspired contemporary interior design that reflects the hotel unique heritage and Thai culture. The 35sqm rooms also enjoy floor-to-ceiling windows overlooking the river and garden."
    #     }
    #     room2 = {
    #         "name" : "Deluxe Balcony Room",
    #         "details" : "Each of these rooms boasts a private 6sqm balcony on which to relax and enjoy views of the bustling river life and the pool. With floor-to-ceiling windows, wooden floors, rugs and furnishings inspired by nature, soft natural tones and Thai décor, these 37sqm rooms add to the overall resort-style ambience."
    #     }
    #     room3 = {
    #         "name" : "Deluxe Premier Room",
    #         "details" : "These 43sqm rooms are located in the River Wing and each boast a large sofa to relax and enjoy river and pool views. Décor is inspired by life on the Chao Phraya river with wooden floors and Thai touches such as teak furniture and beautiful Thai silk fabrics, while a selection of prints from the hotels rich collection of artworks adorn the walls. Both king and twin beds are available."
    #     }
    #     room4 = {
    #         "name" : "Mandarin Room",
    #         "details" : ""
    #     }

# 
room_ChaoPhrayaRoom = Stays("Chao Phraya Room",
                            0,
                            "King Bed",
                            "63SQM / 677SQF",
                            "Bath tub and Japanese toilet";
                            "Complimentary",
                            "Bluetooth Speaker",
                            "Coffee Machine",
                            "Goose Down Bedding by Ploh",    
                            "The ideal choice for guests looking for more space, these large 63sqm rooms incorporate a spacious seating area with a sofa; dining area overlooking both the city and river through floor-to-ceiling windows. The décor is light with soothing aqua and gold tones balanced with a selection of furnishings upholstered in the finest Thai silks, along with a king-size bed swathed in luxurious linen. The room also features a vanity area and walk-in closet.",
                            "Balcony with Seating, Spacious Living with Sofa, Dining Area For 2, 24-Hour Butler Service, Walk-in Closet",
                            "These rooms feature floor-to-ceiling windows that open out to a balcony with views across the city and river. The bedroom incorporates a spacious seating area with a large comfortable sofa and a dining table.",
                            "48 Oriental Avenue Bangkok, 10500 Thailand +66 (0) 2 659 9000")

room_Deluxebalcony = Stays("Deluxe Balcony Room",
                          0,
                          "King Bed",
                          "37SQM / 397SQF"
                          "Japanese Toilets"
                          "Complimentary",
                          "Bluetooth Speaker",
                          "Coffee Machine",
                          "Goose Down Bedding by Ploh",
                          "Each of these rooms boasts a private 6sqm balcony on which to relax and enjoy views of the bustling river life and the pool. With floor-to-ceiling windows, wooden floors, rugs and furnishings inspired by nature, soft natural tones and Thai décor, these 37sqm rooms add to the overall resort-style ambience.",
                          "Floor-To-Ceiling Windows, Balcony with Seating, Bathtub & Walk-In Shower, 24-Hour Butler Service",
                          "Elegant rooms with wooden floors, nature inspired rugs and furnishings with a private balcony and seating area. The rooms offer a Thai touch, giving a unique experience in a resort-style ambience with pool and river views.",
                          "48 Oriental Avenue Bangkok, 10500 Thailand +66 (0) 2 659 9000")

room_Deluxepremier = Stays("Deluxe Premier Room",
                           0,
                           "King Bed/Twin Beds",
                           "43SQM / 463SQF",
                           "Japanese Toilets",
                           "Complimentary",
                           "Bluetooth Speaker",
                           "Coffee Machine",
                           "Goose Down Bedding by Ploh",
                           "These 43sqm rooms are located in the River Wing and each boast a large sofa to relax and enjoy river and pool views. Décor is inspired by life on the Chao Phraya river with wooden floors and Thai touches such as teak furniture and beautiful Thai silk fabrics, while a selection of prints from the hotels rich collection of artworks adorn the walls. Both king and twin beds are available.",
                           "River View, Bathtub & Walk-In Shower, 24-Hour Butler Service, Corner Sofa")
class Rooms(Stays):
    def __init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, number_of_room, contact):
        Stays.__init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, number_of_room, contact)
        self._reserved_room = []
    
    def selected_room(room, suite):
        pass


class Suites(Stays):
    def __init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, number_of_room, contact, bedroom, connecting, powder_room):
        Stays.__init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, number_of_room, contact)
        self._bedroom = bedroom
        self._connecting = connecting
        self._powder_room = powder_room
        self._reserved_room = []
    pass


class RoomCatalog:
    def __init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, room_count, contact):
        Stays.__init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, room_count, contact)
        self.__room_list = []
    
    def selet_room(room, suite):
        pass


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

