import pandas

# all num values are str
df = pandas.read_csv("hotels.csv", dtype={"id": str})
# each dict reps 1 row data
# easy to check when attributes are part of dict
df_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")


class Hotel:
    def __init__(self, input_id):
        self.hotel_id = input_id
        self.name = df.loc[df["id"] == input_id, "name"].squeeze()

    def book(self):
        """Book hotel, then update available to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        # py will not another column index
        df.to_csv("hotels.csv", index=False)

    def available(self):
        # panda has series, 0  "yes". Use squeeze to get the string value
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, client_name, hotel_obj):
        self.hotel_obj = hotel_obj
        self.client_name = client_name

    def generate(self):
        content = f"""
        Thank you for reservation!
        Here are you booking data:
        Name: {self.client_name}
        Hotel: {self.hotel_obj.name}
        """
        print(content)


class CreditCard:
    def __init__(self, num):
        self.num = num

    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.num, "expiration": expiration, "holder": holder, "cvc": cvc}

        if card_data in df_cards:
            return True
        else:
            return False

# main loop
print(df)
hotel_id = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_id)

if hotel.available():
    credit_card = CreditCard(num="1234")
    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        hotel.book()
        name = input("Enter your name: ")
        reservation_ticket = ReservationTicket(client_name=name, hotel_obj=hotel)
        print(reservation_ticket.generate())
    else:
        print("There was a issue with your payment")
else:
    print("Hotel Unavailable.")
