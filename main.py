class Prices:
    def __init__(self):
        self.prices = {}

    def add_price(self, name, price, quantity=1):
        """
        Create price for product based on the quantity
        :param name: product name
        :param price: price of the product
        :param quantity: quantity required
        """
        if len(name) > 1:
            raise ValueError("Products can only contain 1 letter.")

        if price <= 0:
            raise ValueError("Prices must be positive.")

        if quantity < 1:
            raise ValueError("Quantity needs to be > 0.")

        if name not in self.prices:
            self.prices[name] = {}

        self.prices[name][str(quantity)] = price

    @property
    def all_prices(self):
        """
        :return: calculate the highest combination number possible for each product for a discounted price.
        """
        sorted_prices = {}
        for product_name, prices_product in self.prices.items():
            prices_product_sorted = dict(sorted(prices_product.items(), key=lambda x: x[0], reverse=True))
            sorted_prices[product_name] = prices_product_sorted
        return sorted_prices


class Checkout:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        """
        Add products to the basket
        :param item: product
        """
        product_name = item[-1]
        try:
            quantity = int(item[0:-1])
        except ValueError:
            raise ValueError("Quantity needs to be a number.")

        if product_name not in self.items:
            self.items[product_name] = 0
        self.items[product_name] += quantity

    def total(self, prices):
        total_price = 0
        all_prices = prices.all_prices

        for item, quantity in self.items.items():
            prices_item = all_prices.get(item)
            item_total_price = 0

            if not prices_item:
                raise ValueError("This item is not available.")

            for quantity_product, price_product in prices_item.items():
                quantity_product_value = int(quantity_product)
                used_times = quantity // quantity_product_value
                if used_times == 0:
                    continue
                item_total_price += used_times * price_product
                quantity -= used_times * quantity_product_value
                if quantity == 0:
                    break
            total_price += item_total_price

        return total_price
