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