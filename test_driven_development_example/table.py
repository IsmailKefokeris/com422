class Table:

    def __init__(self, table_num, seats, inside, booking=None):
        self.table_num = table_num
        self.seats = seats
        self.inside = inside
        self.booking = booking

    def __str__(self):
        return f"table Num: {self.table_num}, Seats: {self.seats}, Inside? {self.inside}, Booking: {self.booking}"


if __name__ == "__main__":
    t1 = Table(502, 4, True)
