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
        self._contact = "48 Oriental Avenue, Bangkok 10500, Thailand +66 (0) 2 659 9000 mobkk-reservations@mohg.com"
    
    def _showdata(self):
        print(self._name)
        print(self._contact)
        


class Rooms(Stays):
    def __init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, number_of_room):
        Stays.__init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, number_of_room):
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
        Stays.__init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, number_of_room, contact):
        self._reserved_room = []
    
    def selected_room(room, suite):
        pass


class Suites(Stays):
    def __init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, number_of_room, bedroom, connecting, powder_room):
        Stays.__init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, number_of_room)


class Suites(Stays):
    def __init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, number_of_room, contact, bedroom, connecting, powder_room):
        Stays.__init__(self, name, room_number, bed_type, size, toilet_type, complimentary, speaker, coffee_machine, bathrobes, details, highlights, description, number_of_room, contact):
        self._bedroom = bedroom
        self._connecting = connecting
        self._powder_room = powder_room
        self._reserved_room = []
    pass



# all room
room_Chaophraya = Stays(name = "Chao Phraya Room",
                        room_number = 0,
                        bed_type = "King Bed",
                        size = "35SQM / 377SQF",
                        toilet_type = "Japanese Toilets",
                        complimentary = "Complimentary",
                        speaker = "Bluetooth Speaker",
                        coffee_machine = True,
                        bathrobes = "Bathrobes",
                        details = "Located in the Garden Wing, these rooms, with either a flat or split-level layout, offer a residential ambience. The rooms are the epitome of classic elegance with a colonial inspired contemporary interior design that reflects the hotel unique heritage and Thai culture. The 35sqm rooms also enjoy floor-to-ceiling windows overlooking the river and garden.",
                        highlights = "Located in the Garden Wing, Pantry with Large Refrigerator, Living Area, 24-Hour Butler Service",
                        description = "This luxurious room has an entrance area leading to both a spacious and comfortable bedroom and a separate living area with a comfortable sofa."
                        )

room_Deluxebalcony = Stays(name = "Deluxe Balcony Room",
                          room_number = 0,
                          bed_type = "King Bed",
                          size = "37SQM / 397SQF",
                          toilet_type = "Japanese Toilets",
                          complimentary = "Complimentary",
                          speaker = "Bluetooth Speaker",
                          coffee_machine = True,
                          bathrobes = "Bathrobes",
                          details = "Each of these rooms boasts a private 6sqm balcony on which to relax and enjoy views of the bustling river life and the pool. With floor-to-ceiling windows, wooden floors, rugs and furnishings inspired by nature, soft natural tones and Thai décor, these 37sqm rooms add to the overall resort-style ambience.",
                          highlights = "Floor-To-Ceiling Windows, Balcony with Seating, Bathtub & Walk-In Shower, 24-Hour Butler Service",
                          description = "Elegant rooms with wooden floors, nature inspired rugs and furnishings with a private balcony and seating area. The rooms offer a Thai touch, giving a unique experience in a resort-style ambience with pool and river views.",
                        )

room_Deluxepremier = Stays(name = "Deluxe Premier Room",
                           room_number = 0,
                           bed_type = "King Bed / Twin Beds",
                           size = "43SQM / 463SQF",
                           toilet_type = "Japanese Toilets",
                           complimentary = "Complimentary",
                           speaker = "Bluetooth Speaker",
                           coffee_machine = True,
                           bathrobes = "Bathrobes",
                           details = "These 43sqm rooms are located in the River Wing and each boast a large sofa to relax and enjoy river and pool views. Décor is inspired by life on the Chao Phraya river with wooden floors and Thai touches such as teak furniture and beautiful Thai silk fabrics, while a selection of prints from the hotels rich collection of artworks adorn the walls. Both king and twin beds are available.",
                           highlights = "River View, Bathtub & Walk-In Shower, 24-Hour Butler Service, Corner Sofa",
                           description = "Large rooms with sofa and sitting area to relax, offer wooden floors and nature inspired rugs and furnishing with a Thai touch giving a unique experience in a resort style ambiance with views of the river and city."
                            )

room_Madarin = Stays(name = "Mandarin Room",
                     room_number = 0,
                     bed_type = "King Bed",
                     size = "63SQM / 677SQF",
                     toilet_type = "Bath tub and Japanese toilet",
                     complimentary = "Complimentary",
                     speaker = "Bluetooth Speaker",
                     coffee_machine = True,
                     bathrobes = "Bathrobes",
                     details = "The ideal choice for guests looking for more space, these large 63sqm rooms incorporate a spacious seating area with a sofa; dining area overlooking both the city and river through floor-to-ceiling windows. The décor is light with soothing aqua and gold tones balanced with a selection of furnishings upholstered in the finest Thai silks, along with a king-size bed swathed in luxurious linen. The room also features a vanity area and walk-in closet.",
                     highlights = "Balcony with Seating, Spacious Living with Sofa, Dining Area For 2, 24-Hour Butler Service, Walk-in Closet",
                     description = "These rooms feature floor-to-ceiling windows that open out to a balcony with views across the city and river. The bedroom incorporates a spacious seating area with a large comfortable sofa and a dining table."
                    )

room_State = Stays(name = "State Room",
                   room_number = 0,
                   bed_type = "King Bed / Twin Beds",
                   size = "61SQM / 657SQF",
                   toilet_type = "Bath tub and Japanese toilet",
                   complimentary = "Complimentary",
                   speaker = "Bluetooth Speaker",
                   coffee_machine = True,
                   bathrobes = "Bathrobes",
                   details = "Entered via a teak paneled hallway, these rooms are richly decorated in traditional Thai style with dark wood furnishings and brightly coloured Jim Thompson silks. Within the bedroom of these 61sqm rooms there is a seating area furnished with a comfortable sofa and dining table. Large floor-to-ceiling windows open on to a spacious balcony from where guests can enjoy wonderful panoramic river views.",
                   highlights = "Spacious Balcony with River Views, Sumptous Teak Wood Panelling and Floors, Living Area with Sofa, Dining Area For 2",
                   description = "This luxurious rooms offers an amazing Thai experience, the décor features colourful Thai silks by Jim Thompson and teak wood panelling & wooden floors. The rooms are directly river facing & offer dramatic views from the balcony."
                   )

room_JuniorterraceSuite = Stays(name = "Junior Terrace Suite",
                                room_number = 0,
                                bed_type = "King Bed",
                                size = "97SQM / 1,043SQF",
                                toilet_type = "Bath tub and Japanese toilet",
                                complimentary = "complimentary",
                                speaker = "Bluetooth Speaker",
                                coffee_machine = True,
                                bathrobes = "Bathrobes",
                                details = "Ideal for long-staying guests, these large 97sqm junior suites feature a stunning 17sqm terrace that overlooks the river and city. The suite combines a spacious open-plan living area with a large sofa and armchairs, a writing desk and a dining table seating up to five. It is decorated with wooden floors throughout and accented with rugs and prints from the hotel's art collection inspired by the Chao Phraya River.",
                                highlights = "Outdoor Terrace with Seating, Dining Area For 5, Walk-in Closet, 24-Hour Butler Service",
                                description = "This large junior suite is ideal for long-staying guests looking for a large open plan space with a combined sitting and dining area. It features a wonderful terrace of 17sqm/188sqf and a working desk."
                                )

room_DeluxeonebedroomthemeSuite = Stays(name = "Deluxe One-Bedroom Theme Suite",
                                        room_number = 0,
                                        bed_type = "King Bed / Twin Beds",
                                        size = "83SQM / 892SQF",
                                        toilet_type = "Japanese Toilets",
                                        complimentary = "Complimentary",
                                        speaker = "Bose Sound Bar",
                                        coffee_machine = True,
                                        bathrobes = "Silk Kimonos",
                                        details = "Inspired by historic ships of the 1800s that sailed and traded in Bangkok, these 83sqm suites are located on the 16th floor and offer river views and a private 6sqm balcony with seating. Each suite features a spacious living area with a large sofa, wooden floors and a dining table. The large bedroom area has a dressing area with walk-in closet. The bathroom features Italian marble with a walk-in shower and separate bath tub.",
                                        highlights = "Located on High Floor, Balcony with Seating, Spacious Living Room, Dining Area, 24-Hour Butler Service",
                                        description = "This 1-bed suite is on the top floor of the hotel with a balcony offering views of the river. The suite has a large sitting area, a dining table and an additional powder room. The bedroom has a dressing area and a walk in closet."
                                        )

room_Delux2bedroomthemeSuite = Stays(name = "Deluxe 2-Bedroom Theme Suite",
                                        room_number = 0,
                                        bed_type = "King/Twin Beds / Twins/Twin Beds",
                                        size = "125SQM / 1,344SQF",
                                        toilet_type = "Japanese Toilets",
                                        complimentary = "Complimentary",
                                        speaker = "Bose Sound Bar",
                                        coffee_machine = True,
                                        bathrobes = "Silk Kimonos",
                                        details = "The suites feature a spacious living area with a large sofa, beautiful wooden floors, decorated in Thai silks in warm tones. The living area offers a separate sitting and dining areas perfect to relax while at the same time allowing privacy for each room. The Master bedroom has a dressing and sitting area with a large walk in closet. The bathroom features Italian marble with double vanities and a separate shower and bath.",
                                        highlights = "Two Bedrooms, Master Bedroom with Large Walk-in Closet, Balcony with Seating, Spacious Living Room, Dining Area For 4, 24-Hour Butler Service",
                                        description = "An ideal suite for families this two bedroom suite overlooking the pool and the river, features a private balcony with a sitting area. The living area offers separate sitting and dining areas perfect to relax and unwind."
                                        )

room_ChaophrayaSuite = Stays(name = "Chao Phraya Suite",
                             room_number = 0,
                             bed_type = "King Bed",
                             size = "83SQM / 892SQF",
                             toilet_type = "Japanese Toilets",
                             complimentary = "Complimentary",
                             speaker = "Bose Sound Bar",
                             coffee_machine = True,
                             bathrobes = "Silk Kimonos",
                             details = "These spacious 83sqm suites, located in the Garden Wing, have either a flat or split-level layout, floor-to-ceiling windows and a balcony overlooking the river and gardens. The suites feature a colonial-inspired contemporary interior design to reflect the hotel's unique heritage and Thai culture. A separate lounge with dining area is offered alongside a luxurious bedroom and large marble bathroom with separate bathtub, walk-in shower and a walk-in closet",
                             highlights = "Located in the Garden Wing, Flat or Split-level Layout, Dining Room & Lounge Area, Pantry with Large Refrigerator, 24-Hour Butler Service",
                             description = "Floor-to-ceiling windows overlook the river and our gardens. The elegant bedroom features a large marble bathroom with separate bath, a walk-in shower and a walk-in wardrobe. There is also a living area, dining room and balcony."
                            )

room_AuthorsSuite = Stays(name = "Authors' Suites",
                          room_number = 0,
                          bed_type = "King Bed / Twin Beds",
                          size = "101SQM / 1,861SQF",
                          toilet_type = "-",
                          complimentary = "Complimentary",
                          speaker = None,
                          coffee_machine = True,
                          bathrobes = "Silk Kimonos",
                          details = "Individually designed, each 101sqm suite pays tribute in name and ambience, from colour scheme and antique decorations, to one of the celebrated authors who have stayed here. Located in the River Wing, all feature floor-to-ceiling windows and a balcony overlooking the river - perfect for watching river life. Each suite has a spacious sitting room, a bedroom that features a dressing and seating area and a large Italian marble bathroom and walk-in closet.",
                          highlights = "Balcony with River Views, Unique Contemporary Decoration, Spacious Living Area, 24-Hour Butler Service",
                          description = "Located in the River Wing, these suites are tributes to some of the great literary figures that have stayed with us. All feature floor-to-ceiling windows, a balcony, spacious sitting room, a large bathroom and powder room."
                        )

room_DeluxeonebedroomthemeSuite = Stays(name = "Deluxe One-Bedroom Theme Suite",
                                        room_number = 0,
                                        bed_type = "King Bed / Twin Beds",
                                        size = "83SQM / 892SQF",
                                        toilet_type = "Japanese Toilets",
                                        complimentary = "Complimentary",
                                        speaker = "Bose Sound Bar",
                                        coffee_machine = True,
                                        bathrobes = "Silk Kimonos",
                                        details = "Inspired by historic ships of the 1800s that sailed and traded in Bangkok, these 83sqm suites are located on the 16th floor and offer river views and a private 6sqm balcony with seating. Each suite features a spacious living area with a large sofa, wooden floors and a dining table. The large bedroom area has a dressing area with walk-in closet. The bathroom features Italian marble with a walk-in shower and separate bath tub.",
                                        highlights = "Located on High Floor, Balcony with Seating, Spacious Living Room, Dining Area, 24-Hour Butler Service",
                                        description = "This 1-bed suite is on the top floor of the hotel with a balcony offering views of the river. The suite has a large sitting area, a dining table and an additional powder room. The bedroom has a dressing area and a walk in closet.",
                                        )

room_DeluxetwobedroomthemeSuite = Stays(name = "Deluxe Two-Bedroom Theme Suite",
                                        room_number = 0,
                                        bed_type = "King/Twin Beds / Twin/Twin Beds",
                                        size = "125SQM / 1,344SQF",
                                        toilet_type = "Japanese Toilets",
                                        complimentary = "Complimentary",
                                        speaker = "Bose Sound Bar",
                                        coffee_machine = True,
                                        bathrobes = "Silk Kimonos",
                                        details = "These 125sqm two-bedroom Deluxe Suites are ideal for families and overlook the pool and river. Guests can relax and unwind on their private balcony with a seating area, or in the living area that offers separate sitting and dining sections for family and friends to enjoy. The master bedroom has a dressing and sitting area with a large walk-in closet, while the bathroom features Italian marble and a separate shower and bath.",
                                        highlights = "Located on High Floor of River Wing, Balcony with Seating, Interconntecting Room, 24-Hour Butler Service",
                                        description = "An ideal suite for families, this two bedroom suite overlooking the pool and the river, features a private balcony with a sitting area. The living area offers separate sitting and dining areas perfect to relax and unwind"
                                        )

room_Premier1bedroom = Stays(name = "Premier 1-Bedroom Suite",
                            room_number = 0,
                            bed_type = "King Bed / Twin Beds",
                            size = "108SQM / 1,163SQF",
                            toilet_type = "Japanese Toilets",
                            complimentary ="Complimentary",
                            speaker = "Bose Sound Bar",
                            coffee_machine = True,
                            bathrobes = "Silk Kimonos",
                            details = "These spacious 108sqm suites overlook the French Ambassador's residence, with breath-taking views of the Chao Phraya river, a private balcony and sitting area. Elegantly decorated, the Premier Suites have wooden floors in the living and dining areas, complemented perfectly by rugs and prints from the hotel's art collection that are inspired by the River of Kings. The bedroom features a subtle orchid theme, a dressing and sitting area and a walk-in closet.",
                            highlights = "Balcony with Seating, Dining Area For 5, Spacious Living Room and Walk-in Closet, High Bar-style Table, 24-Hour Butler Service",
                            description = "This luxurious suite has an entrance area leading to a spacious sitting area & desk with a separate dining area for 5 people. It has a private balcony with seating area. The specious bedroom has a dressing table and sitting area."
                             )

room_Premier2bedroomSuite = Stays(name = "Premier 2-Bedroom Suite",
                                  room_number = "0",
                                  bed_type = "King/Twin Beds / Twin/Twin Beds",
                                  size = "150SQM / 1,615SQF",
                                  toilet_type = "Japanese Toilets",
                                  complimentary = "Complimentary",
                                  speaker = "Bose Sound Bar",
                                  coffee_machine = True,
                                  bathrobes = "Silk Kimonos",
                                  details = "These spacious 108sqm suites overlook the French Ambassador's residence, with breath-taking views of the Chao Phraya river, a private balcony and sitting area. Elegantly decorated, the Premier Suites have wooden floors in the living and dining areas, complemented perfectly by rugs and prints from the hotel's art collection that are inspired by the River of Kings. The bedroom features a subtle orchid theme, a dressing and sitting area and a walk-in closet.",
                                  highlights = "This large 150sqm suite offers breath-taking river views and is ideal for families who desire additional space and luxury. The separate living area offers both privacy and comfort with a large sofa and a dining area for five guests. The elegant suite features wooden floors in both the living and dining areas, with river inspired rugs and artefacts, as well as prints from the hotel's art collection. It also has a private balcony with sitting area.",
                                  description = "Two Bedrooms, Balcony with Seating, Dining Area For 5, 24-Hour Butler Service"
                                  )

room_SiamonebedroomSuite = Stays(name = "Siam One-Bedroom Suite",
                                 room_number = 0,
                                 bed_type = "King Bed",
                                 size = "107SQM / 1,152SQF",
                                 toilet_type = "Japanese Toilets",
                                 complimentary = "Complimentary",
                                 speaker = "Bose Sound Bar",
                                 coffee_machine = True,
                                 bathrobes = "Silk Kimonos",
                                 details = "Furnished with Thai antiques, magnificent Persian carpets and a varied art collection, this Thai-styled suite is beautifully appointed and eminently comfortable. Large floor-to-ceiling windows open out over the river, while a carved lotus cornice is one of many local touches. The 107sqm suite features a separate living area, as well as a dining area for five guests. Its private balcony with seating area overlooks the river.",
                                 highlights = "Thai Antique Inspired Design from Northern Thailand, Balcony with Seating, Spacious Living Room, Dining Area For 5, Bedroom with Walk-In Wardrobe, 24-Hour Butler Service",
                                 description = "Inspired by the beauty of Northern Thailand, this exquisite one bedroom suite features a separate elegant living and dining spaces, a large King size bed with dressing area. As well as a balcony and sitting area."
                                 )

room_Ambassador2bedroomSuite = Stays(name = "Ambassador 2-Bedroom Suite",
                                     room_number = 0,
                                     bed_type = "King/Twin Beds",
                                     size = "173SQM / 567SQF",
                                     toilet_type = "Japanese Toilets",
                                     complimentary = "Complimentary",
                                     speaker = "Bose Sound Bar",
                                     coffee_machine =  True,
                                     bathrobes = "Silk Kimonos",
                                     details = "Located in the original Oriental Hotel, this unique 173sqm suite exudes luxurious sophistication with beautiful views from a private Victorian-inspired glass conservatory. Lavishly decorated in shades of green and white to exude state grandeur, this expansive suite has two living rooms for ultimate relaxation. The master bedroom connects to a second bedroom making it ideal for families while the bathroom comes complete with rain shower walk-in closet.",
                                     highlights = "Located in historic Authors' Wing, Two living rooms, Private Dining Room with Lounge Area, In-room Private Glass House, 24-Hour Butler Service",
                                     description = "Located in the original 147-year-old Oriental Hotel, the suite exudes luxurious sophistication with beautiful views from a private glass conservatory. Lavishly decorated in shades of greens white to exude a state grandeur."
                                     )

room_Selandia2bedroomSuite = Stays(name = "Selandia Two-Bedroom Suite",
                                   room_number = 0,
                                   bed_type = "King/2 Twins",
                                   size = "169SQM / 1,818SQF",
                                   toilet_type = "Japanese Toilets",
                                   complimentary = "complimentary",
                                   speaker = "Bose Sound Bar",
                                   coffee_machine = True,
                                   bathrobes = "Silk Kimonos",
                                   details = "This two-bedroom suite is named after the Selandia which in 1912 was the world&#39;s first diesel-powered ocean-going ship that travelled from Copenhagen to Bangkok. The 169sqm suite is beautifully decorated in hues of pale ivory against a background of hazy blues and rich scarlets. Furnished with silk throughout, every detail from brass-cornered tables to plush seating exudes luxurious elegance. It features a large living and dining area and two balconies.",
                                   highlights = "Two Bedrooms, Located on a High Floor, Spacious Living Room with Dining Area, Two Balconies with River and City Views, Master Bedroom with Walk-in Closet24-Hour Butler Service",
                                   description = "The Selandia suite features two bedrooms, a very spacious living room, a dining area for 4 persons and study area. There are two balconies and two bathrooms with views over the river and city."                                  
                                )

room_RoyalSuite = Stays(name = "Royal Suite",
                        room_number = 0,
                        bed_type = "King Bed",
                        size = "306SQM / 3,294SQF",
                        toilet_type = "Bath tub and Japanese toilet",
                        complimentary = "complimentary",
                        speaker = "Bose Sound Bar",
                        coffee_machine = True,
                        bathrobes = "Silk Kimonos",
                        details = "Our jewel in the historic crown is the 306sqm Royal Suite designed to suit official and security needs of discerning guests. It offers private access, meeting, fitness and spa facilities, as well as additional bedrooms to accommodate family and entourage. It is decorated in sumptuous royal colours of purples and yellow that juxtapose with white marble and crystal chandeliers for an ambience of classical but understated elegance.",
                        highlights = "Sumptuous, Colourful Regal Design, Private Access, Large Balcony and Dining Area, Private Spa and Fitness Centre, Kitchen, 24-Hour Butler Service",
                        description = "Designed with visiting Royal guests in mind, this suite offers private access, meeting, fitness and spa facilities, as well as an option of additional bedrooms to accommodate entourage, family members or security detail."
                        )

room_Oriental2bedroomSuite = Stays(name = "Oriental 2-Bedroom Suite",
                                   room_number = 0,
                                   bed_type = "King/2 Twins",
                                   size = "376SQM / 4,046SQF",
                                   toilet_type = "Bathtub & Japanese Toilet",
                                   complimentary = "complitmentary",
                                   speaker = "Bose Sound Bar",
                                   coffee_machine = True,
                                   bathrobes = "Silk Kimonos",
                                   details = "This stunning two-bedroom penthouse has welcomed many dignitaries & offers amazing river views with a wrap-around 57.6sqm terrace. Decorated with Thai silks, teak floors & Persian carpets, this suite is ideal for entertaining with a spacious living room with multiple sitting areas, a dining room for 12 and a kitchen. The master bedroom is furnished with antiques and a unique pineapple canopy bed. This 376sqm suite even has its own entertainment room.",
                                   highlights = "Outdoor Terrace with River Views, Master Bedroom with River Views, Fully Equipped Kitchen, Large dining room for 16, Entertainment Room, 24-Hour Butler Service",
                                   description = "This two bedroom penthouse situated on the top floor of the hotel offers amazing full river views with a wrap around terrace of 57.6sqm. It features a private dining room, an entertainment room, multiple sitting areas & a kitchen."
                                   )

#show data
# Stays._showdata(room_Chaophraya)
print(vars(room_Chaophraya))


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

