class Register():

    user_dict = {}

    def __init__(self, fname = '', lname = '', email = '', password1 = '' , password2 = '' , phone_number = ''):
        self._fname = fname
        self._lname = lname
        self._email = email
        self._password1 = password1
        self._password2 = password2
        self._phone_number = phone_number

    def input_data(self):
        self._fname = str(input('Enter First name :'))
        self._lname = str(input('Enter Last name :'))
        self._email = str(input('Enter email :'))
        Register.check_email(self)
        self._password1 = str(input('Enter password :')) 
        self._password2 = str(input('Confirmed password :'))
        if self._password2 != self._password1:
            print('Password Incorrect')
            self._password2 = str(input('Confirmed password :'))
        else:
            pass
        self._phone_number = str(input('Enter phone number :'))

    def add_infomation(self):
        self.user_dict[str(self._fname) + ' ' + str(self._lname)] = [self._email, self._password1, self._phone_number]

    def check_email(self):
        email_list = []
        for value in self.user_dict.values():
            email_list.append(value[0])
        while True:
            if self._email in email_list:
                self._email = str(input('Enter email :'))
            else:
                break
 

register = Register()
register.input_data()
register.add_infomation()
print(register.user_dict)
register.input_data()
register.add_infomation()
print(register.user_dict)
register.input_data()
register.add_infomation()
print(register.user_dict)