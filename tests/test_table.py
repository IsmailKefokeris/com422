import pytest
from test_driven_development_example.table import Table
from test_driven_development_example.restaurant import Restaurant
from test_driven_development_example.Booking import Booking

class TestTableObject:
    def test_table_number(self, default_table):
        assert default_table.table_num == 502

    def test_table_number_of_seats(self, default_table):
        assert default_table.seats == 4

    def test_table_is_table_inside(self, default_table):
        assert default_table.inside == True

class TestRestaurant:

    def test_correct_init_run(self, empty_restaurant):
        assert type(empty_restaurant.tables) is list

    def test_add_table_to_restaurant(self, empty_restaurant, default_table):
        empty_restaurant.add_table(default_table)
        assert len(empty_restaurant.tables) == 1

    def test_successful_remove_table_from_restaurant_by_table_num(self, empty_restaurant, default_table):
        empty_restaurant.add_table(default_table)
        assert empty_restaurant.remove_table(502) == True

    def test_unsuccessful_remove_table_from_restaurant_by_table_num(self, empty_restaurant, default_table):
        empty_restaurant.add_table(default_table)
        assert empty_restaurant.remove_table(504) == False

    def test_successful_book_a_table_in_the_restaurant(self, empty_restaurant, default_table):
        b1 = Booking("John", 3, True)
        empty_restaurant.add_table(default_table)
        assert empty_restaurant.book_table(b1) == True

    def test_unsuccessful_book_a_table_in_the_restaurant_too_many_seats(self, empty_restaurant, default_table):
        b1 = Booking("John", 1, True)
        empty_restaurant.add_table(default_table)
        assert empty_restaurant.book_table(b1) == False

    def test_successful_book_a_table_in_the_restaurant(self, empty_restaurant, default_table, large_table):
        b1 = Booking("John", 8, True)
        empty_restaurant.add_table(default_table)
        empty_restaurant.add_table(large_table)
        assert empty_restaurant.book_table(b1) == True

    def test_successful_book_a_table_and_confirm_its_booked(self, empty_restaurant, default_table, large_table):
        b1 = Booking("John", 8, True)
        empty_restaurant.add_table(default_table)
        empty_restaurant.add_table(large_table)
        empty_restaurant.book_table(b1)
        for table in empty_restaurant.tables:
            if table.table_num == 523:
                assert table.booking == b1





