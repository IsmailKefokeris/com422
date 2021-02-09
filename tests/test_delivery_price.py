from test_driven_development_example.delivery_price import DeliveryPrice


class TestDeliveryPriceHappy:

    def test_delivery_price_is_free(self):
        delivery = DeliveryPrice(10, 101)
        assert delivery.cost() == 0

    def test_delivery_price_is_5_pounds(self):
        delivery = DeliveryPrice(10, 99)
        assert delivery.cost() == 5

    def test_delivery_price_is_10_pounds(self):
        delivery = DeliveryPrice(19, 102)
        assert delivery.cost() == 10

    def test_delivery_price_is_15_pounds(self):
        delivery = DeliveryPrice(29, 102)
        assert delivery.cost() == 15

    def test_delivery_price_is_15_pounds_at_30_miles(self):
        delivery = DeliveryPrice(30, 102)
        assert delivery.cost() == 15

    def test_delivery_price_is_15_pounds_plus_50p_every_mile_above_30_miles(self):
        delivery = DeliveryPrice(35, 102)
        assert delivery.cost() == ((0.5 * 5) + 15)
