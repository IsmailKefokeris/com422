from test_driven_development_example.bus_ticket import BusTicket as Bus

class TestBusTicketHappy:

    def test_bus_ticket_younger_than_3(self):
        ticket = Bus(2)
        assert ticket.bus_ticket_check() == 0

    def test_bus_ticket_half_price_student(self):
        ticket = Bus(18, True)
        assert ticket.bus_ticket_check() == (ticket.normal_price / 2)

    def test_bus_ticket_free_travel_elderly(self):
        ticket = Bus(65)
        assert ticket.bus_ticket_check() == 0

    def test_bus_ticket_normal_price(self):
        ticket = Bus(3)
        assert ticket.bus_ticket_check() == ticket.normal_price
