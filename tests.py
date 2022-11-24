import unittest
from main import Prices, Checkout


class PricesTests(unittest.TestCase):
    def setUp(self):
        self.prices = Prices()

    def test_product_many_letters(self):
        self.assertRaises(ValueError, self.prices.add_price, 'AB', 10)

    def test_negative_price(self):
        self.assertRaises(ValueError, self.prices.add_price, 'A', -6)

    def test_negative_quantity(self):
        self.assertRaises(ValueError, self.prices.add_price, 'A', 50, -8)


class CheckoutTests(unittest.TestCase):
    def setUp(self):
        self.prices = Prices()
        self.prices.add_price('A', 50)
        self.prices.add_price('A', 130, 3)
        self.prices.add_price('B', 30)
        self.prices.add_price('B', 45, 2)
        self.prices.add_price('C', 10)

    def test_checkout_no_items(self):
        checkout = Checkout()
        self.assertEqual(checkout.total(self.prices), 0)

    def test_checkout_wrong_quantity(self):
        checkout = Checkout()
        self.assertRaises(ValueError, checkout.add_item, "EA")

    def test_checkout_missing_item(self):
        checkout = Checkout()
        checkout.add_item('1A')
        checkout.add_item('1E')
        self.assertRaises(ValueError, checkout.total, self.prices)

    def test_checkout_1(self):
        checkout = Checkout()
        checkout.add_item('1A')
        self.assertEqual(checkout.total(self.prices), 50)

    def test_checkout_2(self):
        checkout = Checkout()
        checkout.add_item('1A')
        checkout.add_item('1A')
        self.assertEqual(checkout.total(self.prices), 100)

    def test_checkout_3(self):
        checkout = Checkout()
        checkout.add_item('1A')
        checkout.add_item('1B')
        self.assertEqual(checkout.total(self.prices), 80)

    def test_checkout_4(self):
        checkout = Checkout()
        checkout.add_item('1A')
        checkout.add_item('1B')
        checkout.add_item('1C')
        self.assertEqual(checkout.total(self.prices), 90)

    def test_checkout_5(self):
        checkout = Checkout()
        checkout.add_item('1A')
        checkout.add_item('1A')
        checkout.add_item('1A')
        checkout.add_item('1B')
        self.assertEqual(checkout.total(self.prices), 160)


if __name__ == "__main__":
    unittest.main()
