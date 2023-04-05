
class Account():

    def __init__(self, fname = None, lname = None, password1 = None, password2 = None, phone_number = None):
        self._fname = fname
        self._lname = lname
        self._password1 = password1
        self._password2 = password2
        self._phone_number = phone_number
    @property
    def fname(self):
        return self._fname

    @fname.setter
    def set_fname (self,new_fname):
        self._fname = new_fname 

class System():
    def __init__(self):
        self._account_list = []
    
    def add_account (self, user):
        self._account_list.append(user)
        print(self._account_list)
    
    def create_user(self, fname, lname, email, password, phone_number):
        new_user = Account(fname, lname, email, password, phone_number)
        self.add_account(user = new_user)

    @property
    def acc_list(self):
        return self._account_list
