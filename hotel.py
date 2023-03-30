class Hotel:
    def __init__(self, name, branch, location):
        self.__name = name
        self.__branch = branch
        self.__location = location
    pass

class Contact:
    def __init__(self, header_info, general_enquires, reservation, sales_marketing, dining, weddings, events, spa):
        self.__header_info = header_info
        self.__general_enquires = general_enquires
        self.__reservation = reservation
        self.__sales_marketing = sales_marketing
        self.__dining = dining
        self.__weddings = weddings
        self.__events = events
        self.__spa = spa
    pass