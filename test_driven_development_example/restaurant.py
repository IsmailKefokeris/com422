from test_driven_development_example.table import Table
from test_driven_development_example.Booking import Booking


class Restaurant:

    def __init__(self):
        self.tables = []
        self.acceptable_empty_seats = 2

    def add_table(self, table):
        self.tables.append(table)

    def remove_table(self, num):
        for table in self.tables:
            if table.table_num == num:
                del table
                return True
        return False

    def book_table(self, booking):
        for table in self.tables:
            if table.booking is None:
                if 0 <= (table.seats - booking.guest_num) <= self.acceptable_empty_seats \
                        and table.inside == booking.inside:
                    table.booking = booking
                    return True
        return False

if __name__ == "__main__":
    t1 = Table(523, 5, True)
    t2 = Table(902, 4, True)
    t3 = Table(202, 10, True)
    t4 = Table(101, 8, True)

    r1 = Restaurant()

    r1.add_table(t1)
    r1.add_table(t2)
    r1.add_table(t3)
    r1.add_table(t4)

    b1 = Booking("James", 5, True)

    r1.book_table(b1)