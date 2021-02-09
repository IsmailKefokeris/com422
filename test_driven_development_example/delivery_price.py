class DeliveryPrice:

    def __init__(self, distance, item_price):
        self.distance = distance
        self.item_price = item_price
        self.delivery_cost = 0

    def cost(self):
        if self.distance <= 10:
            if self.item_price > 100:
                return self.delivery_cost
            elif self.item_price < 100:
                self.delivery_cost = 5
                return self.delivery_cost
        elif 10 < self.distance < 20:
            self.delivery_cost = 10
            return self.delivery_cost
        elif 20 <= self.distance < 30:
            self.delivery_cost = 15
            return self.delivery_cost
        elif self.distance >= 30:
            self.delivery_cost = 15
            for p in range(30, self.distance, 1):
                self.delivery_cost += 0.5
            return self.delivery_cost

