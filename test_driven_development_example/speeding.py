class SpeedingTicket:

    def __init__(self, speedlimit, driverspeed):
        self.speed_limit = speedlimit
        self.driver_speed = driverspeed
        self.ticket = False
        self.summons = False

    def issue_ticket(self):
        if (self.driver_speed - self.speed_limit) == 10:
            self.ticket = True
            self.summons = True
            return self.ticket, self.summons
        elif (self.driver_speed - self.speed_limit) != 10:
            self.ticket = True
            return self.ticket, self.summons

        return self.ticket, self.summons

