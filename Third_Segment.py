class Booking:
    def __init__(self, calendar, check_in, check_out, room_price, total_price, currency):
        self.__calendar = calendar
        self.__check_in = check_in
        self.__check_out = check_out
        self.__room_price = room_price
        self.__total_price = total_price
        self.__currency = currency
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
    pass