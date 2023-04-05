class Account():

    user_dict = {}
    login_email = None
    login_password = None
    email_list = []
    password_list = []

    def __init__(self, fname = '', lname = '', email = '', password1 = '' , password2 = '' , phone_number = ''):
        self._fname = fname
        self._lname = lname
        self._email = email
        self._password1 = password1 
        self._password2 = password2
        self._phone_number = phone_number

    def register(self):
        self.input_register()
        self.add_infomation()

    def login(self):
        self.input_login()
        self.check_login(self.login_email, self.login_password)

    def input_register(self):
        self._fname = str(input('Enter First name :'))
        self._lname = str(input('Enter Last name :'))
        self._email = str(input('Enter email :'))
        self.check_used_email()
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
        for value in self.user_dict.values(): #สร้าง list เก็บ email
            self.email_list.append(value[0])
        for value in self.user_dict.values(): #สร้าง list เก็บ password
            self.password_list.append(value[1])
        print(self.user_dict)

    def check_used_email(self):
        # for value in self.user_dict.values():
        #     self.email_list.append(value[0])
        while True:
            if self._email in self.email_list:
                print('Email used!')
                self._email = str(input('Enter email :'))
            else:
                break
        
    def input_login(self):
        self.login_email = str(input('Enter email :'))
        self.login_password = str(input('Enter password :'))
        return self.login_email, self.login_password

    def check_login(self, login_email, login_password):
        # for value in self.user_dict.values():
        #     self.password_list.append(value[1])
        if login_email in self.email_list:
            # print('a')
            while True:
                if login_password in self.password_list:
                    if self.password_list.index(login_password) == self.email_list.index(login_email):
                        print('Login!')
                        break
                    else:
                        print('Invalid Password')
                        login_password = str(input('Enter password :'))

class System():
    def __init__(self):
        self.__account_list = []
    
    def add_account (self, user):
        self.__account_list.append(user)
         
class User():
    def register(self):
        pass

test =  Account()
test.register()
test.register()
test.login()

