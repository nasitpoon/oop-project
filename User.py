from registor import Register
class User:
    def __init__(self, email, password, status):
        self._email = email
        self._password = password
        self._status = status

    def watch_rooms():
        pass

class Member(User):
    def __init__(self, email = '', password = '', status = '', member_id = ''):
        self._member_id = member_id
        super().__init__(email, password, status)
    
    def login(self, member_id = '', max_attempts = 3) -> bool:
        self._member_id = member_id
        attempts = 0
        # super().__init__(email,password,self._member_id)
        while(attempts <= max_attempts):
            self._email = str(input('Enter email : '))
            self._password = str(input('Enter password : '))
            if self._email in Register.user_email_password.keys():
                print('Has email')
                print(Register.user_email_password[self._email],self._password)
                # check password
                if Register.user_email_password[self._email][0] == self._password:
                    print('pass')
                    break
                else:
                    print('Your password is not correct')
                    attempts+=1
            elif self._email not in Register.user_email_password.keys():
                    print('Not have this email')
                    
        print("Max login attempts exceeded")


    def select_room(start_date, end_date):
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

test = Member(User)
test.login()
test1 = Member(User)
