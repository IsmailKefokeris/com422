from test_driven_development_example.speeding import SpeedingTicket

class TestSpeedingTicket:

    def test_speeding_ticket_issued_and_court_summoned(self):
        ticket = SpeedingTicket(70, 80)
        assert ticket.issue_ticket() == (True, True)

    def test_speeding_ticket_issued_but_no_court_summons(self):
        ticket = SpeedingTicket(70, 75)
        assert ticket.issue_ticket() == (True, False)