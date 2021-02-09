
class Booking:

    def __init__(self, name, guest_num, inside):
        self.name = name
        self.guest_num = guest_num
        self.inside = inside

    def __repr__(self):
        return f"Name: {self.name}, Guests: {self.guest_num}, Inside? {self.inside}"