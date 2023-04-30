import pandas

df = pandas.read_csv("hotels.csv")


class Hotel:
    def __init__(self, id_hotel):
        pass

    def book(self):
        pass

    def availble(self):
        pass


class ReservationTicket:
    def __init__(self, client_name, hotel_obj):
        pass

    def generate(self):
        pass


print(df)
id_hotel = input("Enter the id of the hotel: ")
hotel = Hotel(id)
if hotel.availble():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel Unavailable.")