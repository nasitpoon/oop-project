class Payment:
    def __init__(self,title = '', first_name = '', last_name = '', email = '', email_confirmation = '', country = '', phone_number = '', street_address = '', city = '', state_province = '', postal_code = '',date_of_birth = '', additional_info = '', terms_conditions = '', unpaid = '', day = '', month = ''):
        self._title = title
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
        self._day = day
        self._month = month

    def customer_info(self):
        # self._title = str(input('Enter title : '))
        # self._first_name = str(input('Enter first name : '))
        # self._last_name = str(input('Enter last name : '))
        # self._email = str(input('Enter email : '))
        # self._email_confirmation = str(input('Enter email confirmation : '))
        # Payment.checkemail(self)
        # self._country = str(input('Enter country : '))
        # self._phone_number = str(input("Enter phone number : "))
        # self._street_address = str(input('Enter street address : '))
        # self._city = str(input('Enter city : '))
        # self._state_province = str(input('Enter state province : '))
        # self._postal_code = str(input('Enter postal : '))
        self._date_of_birth = Payment.birthday(self)
        # self._additional_info = str(input('Enter additional info : '))
        # self._terms_conditions = str(input('Enter terms and conditions : '))
        # self._unpaid = str(input('Enter unpaid : '))

        # print(self._date_of_birth)

    def checkemail(self):
        while(True):
            if self._email == self._email_confirmation:
                print("Correct")
                return False
            else:
                print('Email or Email confirmation is not correct')
                self._email = str(input('Enter email : '))
                self._email_confirmation = str(input('Enter email confirmation : '))
                

    def birthday(self):
        self._month = int(input('Enter month : '))
        while(self._month > 12 or self._month < 1):
            self._month = int(input('Enter month : '))
        self._day = int(input('Enter day : '))
        while(self._day > 31):
            self._day = int(input('Enter day : '))

# class that pay by credit card
class CreditPayment:
    def __init__(self, card_number = None, cardholder_name = None, expiration_date = None):
        self._card_number = card_number
        self._cardholder_name = cardholder_name
        self._expiration_date = expiration_date

        # print(self._expiration_date)

class SpecialCode:
    def __init__(self, iata_number, promo_code, group_code):
        self._iata_number = iata_number
        self._promo_code = promo_code
        self._group_code = group_code
        
    def insert_specialcode(self):
        self._iata_number = str(input('Enter Iata number :'))
        self._promo_code = str(input('Enter Promotion code :'))
        self._group_code = str(input('Enter Group code :'))

class CreditCard:
    def __init__(self,card_number = '',card_holder_name = '',expiration_date = ''):
        self._card_number = card_number
        self._cardholder_name = card_holder_name
        self._expiration_date = expiration_date

    def expire(self):
        self.month = int(input('Enter month : '))
        while(True):
            if self.month <= 12:
                # print(f'month = {self.month}')
                self.year = int(input('Enter year : '))
                return self.month,self.year
            else:
                self.month = int(input('Enter month : '))



    def card_info(self):
        self._cardholder_name = str(input('Enter Cardholder name : '))
        self._card_number = str(input('Enter Card number : '))
        while len(self._card_number) != 16:
            print("Not correct")
            self._card_number = str(input('Enter Card number : '))
        else: pass
        self._expiration_date = CreditCard.expire(self)

class PaymentInfo:
    pass


# test = CreditCard()
# test.card_info()

test = Payment()
test.customer_info()
