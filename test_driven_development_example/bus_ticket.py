

class BusTicket:

    def __init__(self, age, student=None):
        self.age = age
        self.student = student
        self.normal_price = 4
        self.paying = 0

    def bus_ticket_check(self):
        if self.age < 3 or self.age >= 65:
            return self.paying
        elif self.student and self.age < 19:
            self.paying = self.normal_price / 2
            return self.paying

        return self.normal_price


