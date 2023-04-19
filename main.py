from SearchRoom import RoomCatalog
from Booking import Booking, BookingHistory
from User import Admin, User, Member
from Payment import Payment
from fastapi import FastAPI
import Roominstance as r

app = FastAPI()



Catalog = RoomCatalog()
admin = Admin('','','')
admin.add_room(Catalog, r.room_Deluxebalcony)
admin.add_room(Catalog, r.room_AuthorsSuite)
admin.add_room(Catalog, r.room_Deluxepremier)
admin.add_room(Catalog, r.room_Mandarin)
admin.add_room(Catalog, r.room_Chaophraya)
admin.add_room(Catalog, r.room_State)
admin.add_room(Catalog, r.room_JuniorterraceSuite)
admin.add_room(Catalog, r.room_ChaophrayaSuite)
admin.add_room(Catalog, r.room_Deluxe1bedroomSuite)
admin.add_room(Catalog, r.room_Deluxe2bedroomSuite)
admin.add_room(Catalog, r.room_Deluxe1bedroomthemeSuite)
admin.add_room(Catalog, r.room_Deluxe2bedroomthemeSuite)
admin.add_room(Catalog, r.room_Premier1bedroom)
admin.add_room(Catalog, r.room_Premier2bedroomSuite)
admin.add_room(Catalog, r.room_Siam1bedroomSuite)
admin.add_room(Catalog, r.room_Ambassador2bedroomSuite)
admin.add_room(Catalog, r.room_Selandia2bedroomSuite)
admin.add_room(Catalog, r.room_RoyalSuite)
admin.add_room(Catalog, r.room_Oriental2bedroomSuite)


# for i in range(len(Catalog.user_select("Stays"))):
#     print(Catalog.user_select("Stays")[i].get_name())

# for i in range(len(u1.watch_rooms(Catalog, "Stays"))):
#     print(u1.watch_rooms(Catalog, "Stays")[i].get_name())

admin.update_price(r.room_Ambassador2bedroomSuite, 34000)
admin.update_price(r.room_Oriental2bedroomSuite, 89000)
admin.update_price(r.room_RoyalSuite, 45000)
admin.update_price(r.room_Selandia2bedroomSuite, 56000)
admin.update_price(r.room_Ambassador2bedroomSuite, 34000)
admin.update_price(r.room_Oriental2bedroomSuite, 89000)
admin.update_price(r.room_RoyalSuite, 45000)
admin.update_price(r.room_Selandia2bedroomSuite, 56000)
admin.update_price(r.room_Ambassador2bedroomSuite, 34000)
admin.update_price(r.room_Oriental2bedroomSuite, 89000)
admin.update_price(r.room_RoyalSuite, 45000)
admin.update_price(r.room_Selandia2bedroomSuite, 56000)

# m1 = Member('Vivat', 'Techakosol', 'nickvivat@hotmail.com', 'n', '0915752833')
# p1 = Payment(m1, 8235000, 'Credit')
# b1 = Booking("1-1-2019", "1-1-2020", "Deluxe Balcony Room", m1, p1)
# b1.make_payment(p1)
# m2 = Member('Nasit', 'Phalunchai', 'nasitpoon@gmail.com', 'p', '0821235479')
# p2 = Payment(m2, 67500, 'Credit')
# b2 = Booking("2-1-2019", "4-1-2019", "Deluxe Balcony Room", m2, p2)
# m3 = Member('Patt', 'Prom', 'pattprom@gmail.com', 'pp', '0925478366')
# p3 = Payment(m3, 652500, 'Credit')
# b3 = Booking("2-2-2022", "2-3-2022", "Deluxe Balcony Room", m3, p3)

h = BookingHistory()

# h.add_book(b1)
# h.add_book(b2)
# h.add_book(b3)
print(h)

@app.get("/login")
async def login(fname : str, lname : str, email : str, password : str, phone : str):
    global m1
    m1 = Member(fname, lname, email, password, phone)
    return m1

@app.get("/payment")
async def payment(total_cost : int, method : str):
    global p1
    p1 = Payment(m1, total_cost, method)
    return p1


@app.get("/booking")
async def booking(start_date : str, end_date : str, room_type : str):
    b1 = Booking(start_date, end_date, room_type, m1, p1)
    b1.make_payment(p1)
    h.add_book(b1)

    return b1



@app.get("/booking_history")
async def booking_history():
    
    return {"data" : h}

