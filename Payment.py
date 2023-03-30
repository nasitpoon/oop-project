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

class CreditCard:
    def __init__(self):
        pass

    def card_info():
        pass

class PaymentInfo:
    pass