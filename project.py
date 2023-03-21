from enum import Enum

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
    
    def all_room():
        room1 = {
            "name" : "Chao Phraya Room",
            "details" : "Located in the Garden Wing, these rooms with either a flat or split-level layout, offer a residential ambience. The rooms are the epitome of classic elegance with a colonial inspired contemporary interior design that reflects the hotel unique heritage and Thai culture. The 35sqm rooms also enjoy floor-to-ceiling windows overlooking the river and garden."
        }
        room2 = {
            "name" : "Deluxe Balcony Room",
            "details" : "Each of these rooms boasts a private 6sqm balcony on which to relax and enjoy views of the bustling river life and the pool. With floor-to-ceiling windows, wooden floors, rugs and furnishings inspired by nature, soft natural tones and Thai décor, these 37sqm rooms add to the overall resort-style ambience."
        }
        room3 = {
            "name" : "Deluxe Premier Room",
            "details" : "These 43sqm rooms are located in the River Wing and each boast a large sofa to relax and enjoy river and pool views. Décor is inspired by life on the Chao Phraya river with wooden floors and Thai touches such as teak furniture and beautiful Thai silk fabrics, while a selection of prints from the hotels rich collection of artworks adorn the walls. Both king and twin beds are available."
        }
        room4 = {
            "name" : "Mandarin Room",
            "details" : ""
        }


class Rooms(Stays):
    def __init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, number_of_room):
        Stays.__init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, number_of_room)
        self._reserved_room = []
    
    def selected_room(room, suite):
        pass

class Suites(Stays):
    def __init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, number_of_room, bedroom, connecting, powder_room):
        Stays.__init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, number_of_room)
        self._bedroom = bedroom
        self._connecting = connecting
        self._powder_room = powder_room
        self._reserved_room = []
    pass


# all room
room_Chaophraya = Stays("Chao Phraya Room",
                        0,
                        "King Bed",
                        "35SQM / 377SQF",
                        "Japanese Toilets",
                        "Complimentary",
                        "Bluetooth Speaker",
                        "Coffee Machine",
                        "Bathrobes",
                        "Located in the Garden Wing, these rooms, with either a flat or split-level layout, offer a residential ambience. The rooms are the epitome of classic elegance with a colonial inspired contemporary interior design that reflects the hotel unique heritage and Thai culture. The 35sqm rooms also enjoy floor-to-ceiling windows overlooking the river and garden.",
                        "Located in the Garden Wing, Pantry with Large Refrigerator, Living Area, 24-Hour Butler Service",
                        "This luxurious room has an entrance area leading to both a spacious and comfortable bedroom and a separate living area with a comfortable sofa."
                        )

# Stays._showdata(room_Chaophraya)

room_Deluxebalcony = Stays("Deluxe Balcony Room",
                          0,
                          "King Bed",
                          "37SQM / 397SQF"
                          "Japanese Toilets"
                          "Complimentary",
                          "Bluetooth Speaker",
                          "Coffee Machine",
                          "Bathrobes",
                          "Each of these rooms boasts a private 6sqm balcony on which to relax and enjoy views of the bustling river life and the pool. With floor-to-ceiling windows, wooden floors, rugs and furnishings inspired by nature, soft natural tones and Thai décor, these 37sqm rooms add to the overall resort-style ambience.",
                          "Floor-To-Ceiling Windows, Balcony with Seating, Bathtub & Walk-In Shower, 24-Hour Butler Service"
                          "Elegant rooms with wooden floors, nature inspired rugs and furnishings with a private balcony and seating area. The rooms offer a Thai touch, giving a unique experience in a resort-style ambience with pool and river views."
                            )

room_Deluxepremier = Stays("Deluxe Premier Room",
                           0,
                           "King Bed / Twin Beds",
                           "43SQM / 463SQF",
                           "Japanese Toilets",
                           "Complimentary",
                           "Bluetooth Speaker",
                           "Coffee Machine",
                           "Bathrobes",
                           "These 43sqm rooms are located in the River Wing and each boast a large sofa to relax and enjoy river and pool views. Décor is inspired by life on the Chao Phraya river with wooden floors and Thai touches such as teak furniture and beautiful Thai silk fabrics, while a selection of prints from the hotels rich collection of artworks adorn the walls. Both king and twin beds are available.",
                           "River View, Bathtub & Walk-In Shower, 24-Hour Butler Service, Corner Sofa",
                           "Large rooms with sofa and sitting area to relax, offer wooden floors and nature inspired rugs and furnishing with a Thai touch giving a unique experience in a resort style ambiance with views of the river and city."
                            )

room_Madarin = Stays("Mandarin Room",
                     0,
                     "King Bed",
                     "63SQM / 677SQF",
                     "Bath tub and Japanese toilet",
                     "Complimentary",
                     "Bluetooth Speaker",
                     "Coffee Machine",
                     "Bathrobes",
                     "The ideal choice for guests looking for more space, these large 63sqm rooms incorporate a spacious seating area with a sofa; dining area overlooking both the city and river through floor-to-ceiling windows. The décor is light with soothing aqua and gold tones balanced with a selection of furnishings upholstered in the finest Thai silks, along with a king-size bed swathed in luxurious linen. The room also features a vanity area and walk-in closet.",
                     "Balcony with Seating, Spacious Living with Sofa, Dining Area For 2, 24-Hour Butler Service, Walk-in Closet",
                     "These rooms feature floor-to-ceiling windows that open out to a balcony with views across the city and river. The bedroom incorporates a spacious seating area with a large comfortable sofa and a dining table."
                    )

room_State = Stays("State Room",
                   0,
                   "King Bed / Twin Beds",
                   "61SQM / 657SQF",
                   "Bath tub and Japanese toilet",
                   "Complimentary",
                   "Bluetooth Speaker",
                   "Coffee Machine",
                   "Bathrobes",
                   "Entered via a teak paneled hallway, these rooms are richly decorated in traditional Thai style with dark wood furnishings and brightly coloured Jim Thompson silks. Within the bedroom of these 61sqm rooms there is a seating area furnished with a comfortable sofa and dining table. Large floor-to-ceiling windows open on to a spacious balcony from where guests can enjoy wonderful panoramic river views.",
                   "Spacious Balcony with River Views, Sumptous Teak Wood Panelling and Floors, Living Area with Sofa, Dining Area For 2",
                   "This luxurious rooms offers an amazing Thai experience, the décor features colourful Thai silks by Jim Thompson and teak wood panelling & wooden floors. The rooms are directly river facing & offer dramatic views from the balcony."
                   )

room_Juniorterracesuite = Stays("Junior Terrace Suite",
                                0,
                                "King Bed",
                                "97SQM / 1,043SQF",
                                "Bath tub and Japanese toilet",
                                "complimentary",
                                "Bluetooth Speaker",
                                "Coffee Machine",
                                "Bathrobes",
                                "Ideal for long-staying guests, these large 97sqm junior suites feature a stunning 17sqm terrace that overlooks the river and city. The suite combines a spacious open-plan living area with a large sofa and armchairs, a writing desk and a dining table seating up to five. It is decorated with wooden floors throughout and accented with rugs and prints from the hotel's art collection inspired by the Chao Phraya River.",
                                "Outdoor Terrace with Seating, Dining Area For 5, Walk-in Closet, 24-Hour Butler Service",
                                "This large junior suite is ideal for long-staying guests looking for a large open plan space with a combined sitting and dining area. It features a wonderful terrace of 17sqm/188sqf and a working desk."
                                )

room_Deluxeonebedroomthemesuite = Stays("Deluxe One-Bedroom Theme Suite",
                                        0,
                                        "King Bed / Twin Beds",
                                        "83SQM / 892SQF",
                                        "Japanese Toilets",
                                        "Complimentary",
                                        "Bose Sound Bar",
                                        "Coffee Machine",
                                        "Silk Kimonos",
                                        "Inspired by historic ships of the 1800s that sailed and traded in Bangkok, these 83sqm suites are located on the 16th floor and offer river views and a private 6sqm balcony with seating. Each suite features a spacious living area with a large sofa, wooden floors and a dining table. The large bedroom area has a dressing area with walk-in closet. The bathroom features Italian marble with a walk-in shower and separate bath tub.",
                                        "Located on High Floor, Balcony with Seating, Spacious Living Room, Dining Area, 24-Hour Butler Service",
                                        "This 1-bed suite is on the top floor of the hotel with a balcony offering views of the river. The suite has a large sitting area, a dining table and an additional powder room. The bedroom has a dressing area and a walk in closet."
                                        )

room_Delux2bedroomthemesuite = Stays("Deluxe 2-Bedroom Theme Suite",
                                        0,
                                        "King/Twin Beds / Twins/Twin Beds",
                                        "125SQM / 1,344SQF",
                                        "Japanese Toilets",
                                        "Complimentary",
                                        "Bose Sound Bar",
                                        "Coffee Machine",
                                        "Silk Kimonos",
                                        "The suites feature a spacious living area with a large sofa, beautiful wooden floors, decorated in Thai silks in warm tones. The living area offers a separate sitting and dining areas perfect to relax while at the same time allowing privacy for each room. The Master bedroom has a dressing and sitting area with a large walk in closet. The bathroom features Italian marble with double vanities and a separate shower and bath.",
                                        "Two Bedrooms, Master Bedroom with Large Walk-in Closet, Balcony with Seating, Spacious Living Room, Dining Area For 4, 24-Hour Butler Service",
                                        "An ideal suite for families this two bedroom suite overlooking the pool and the river, features a private balcony with a sitting area. The living area offers separate sitting and dining areas perfect to relax and unwind."
                                        )

room_Chaophrayasuite = Stays("Chao Phraya Suite",
                             0,
                             "King Bed",
                             "83SQM / 892SQF",
                             "Japanese Toilets",
                             "Complimentary",
                             "Bose Sound Bar",
                             "Coffee Machine",
                             "Silk Kimonos",
                             "These spacious 83sqm suites, located in the Garden Wing, have either a flat or split-level layout, floor-to-ceiling windows and a balcony overlooking the river and gardens. The suites feature a colonial-inspired contemporary interior design to reflect the hotel's unique heritage and Thai culture. A separate lounge with dining area is offered alongside a luxurious bedroom and large marble bathroom with separate bathtub, walk-in shower and a walk-in closet",
                             "Located in the Garden Wing, Flat or Split-level Layout, Dining Room & Lounge Area, Pantry with Large Refrigerator, 24-Hour Butler Service",
                             "Floor-to-ceiling windows overlook the river and our gardens. The elegant bedroom features a large marble bathroom with separate bath, a walk-in shower and a walk-in wardrobe. There is also a living area, dining room and balcony."
                            )

room_Authorssuite = Stays("Authors' Suites",
                          0,
                          "King Bed / Twin Beds",
                          "101SQM / 1,861SQF",
                          "-",
                          "Complimentary",
                          "-",
                          "Coffee Machine",
                          "Silk Kimonos",
                          "Individually designed, each 101sqm suite pays tribute in name and ambience, from colour scheme and antique decorations, to one of the celebrated authors who have stayed here. Located in the River Wing, all feature floor-to-ceiling windows and a balcony overlooking the river - perfect for watching river life. Each suite has a spacious sitting room, a bedroom that features a dressing and seating area and a large Italian marble bathroom and walk-in closet.",
                          "Balcony with River Views, Unique Contemporary Decoration, Spacious Living Area, 24-Hour Butler Service",
                          "Located in the River Wing, these suites are tributes to some of the great literary figures that have stayed with us. All feature floor-to-ceiling windows, a balcony, spacious sitting room, a large bathroom and powder room."
                        )

room_Deluxeonebedroomthemesuite = Stays("Deluxe One-Bedroom Theme Suite",
                                        0,
                                        "King Bed / Twin Beds",
                                        "83SQM / 892SQF",
                                        "Japanese Toilets",
                                        "Complimentary",
                                        "Bose Sound Bar",
                                        "Coffee Machine",
                                        "Silk Kimonos",
                                        "Inspired by historic ships of the 1800s that sailed and traded in Bangkok, these 83sqm suites are located on the 16th floor and offer river views and a private 6sqm balcony with seating. Each suite features a spacious living area with a large sofa, wooden floors and a dining table. The large bedroom area has a dressing area with walk-in closet. The bathroom features Italian marble with a walk-in shower and separate bath tub.",
                                        "Located on High Floor, Balcony with Seating, Spacious Living Room, Dining Area, 24-Hour Butler Service",
                                        "This 1-bed suite is on the top floor of the hotel with a balcony offering views of the river. The suite has a large sitting area, a dining table and an additional powder room. The bedroom has a dressing area and a walk in closet."
                                        )


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
