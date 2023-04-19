import uuid
from ClassStays import Room
from DateCal import DateCal
    

class Booking:
    existing_booking_ids = set()
    counter = 0

    def __init__(self, start_date, end_date, room_type, member, payment):
        self.__booking_id = Booking.generate_booking_id()
        self.__status = "PENDING"
        self.__start_date = start_date
        self.__end_date = end_date
        self.__nights = DateCal().date_diff(start_date, end_date)
        self.__room_price = 22500
        self.__total_cost = self.__room_price * self.__nights
        self.__room_number = Room().get_room_number()
        self.__room_type = room_type
        self.__member_info = {"member_id": member.get_member_id(),"name": member.get_name(), "email": member.get_email(), "phone": member.get_phone()}
        self.__payment_info = {"method": payment.get_method(), "transaction_id": payment.get_transaction_id(), "amount": payment.get_amount(), "date_time": payment.get_date()}
        Booking.counter += 1
        self.__booking_number = Booking.counter

    
    @classmethod
    def generate_booking_id(cls):
        while True:
            booking_id = str(uuid.uuid4().hex)[:8]
            if booking_id not in cls.existing_booking_ids:
                cls.existing_booking_ids.add(booking_id)
                return booking_id
            

    def make_payment(self, payment):
        # Make a payment for the total cost of the booking
        if payment.get_amount() != self.__total_cost:
            raise ValueError('Payment amount does not match total cost of booking')
        payment.process_payment()
        self.__status = 'CONFIRMED'
        self.__payment = payment

    
    def __str__(self):
        return f"Booking {self.__booking_number}: booking_id = {self.__booking_id}, start_date = {self.__start_date}, end_date = {self.__end_date}, nights = {self.__nights}, room_price = {self.__room_price}, total_price = {self.__total_cost}, room_number = {self.__room_number}\n           room_type = {self.__room_type}, details = {self.__member_info}\n           payment_info = {self.__payment_info}\n"
    

    def booked_info(self):
        pass


class BookingHistory:
    def __init__(self):
        self.__book_history = []

    def add_book(self, booking):
        self.__book_history.append(booking)

    def __str__(self):
        if not self.__book_history:
            return "No bookings yet"
        else:
            return "\n".join(str(booking) for booking in self.__book_history)

class SelectedRoom:
    pass


class ManageBooking:
    pass