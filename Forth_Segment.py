class Member(User):
    def __init__(self, email, password, status, member_id):
        User.__init__(self, email, password, status)
        self.__member_id = member_id
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
    pass

