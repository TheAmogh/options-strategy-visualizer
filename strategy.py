from datetime import date

from option import Option
from order import Order


class Strategy:
    option_orders = None

    def __init__(self):
        self.option_orders = []

    def __repr__(self):
        return f"{self.option_orders}"

    def add_order(self, order: Order):
        self.option_orders.append(order)
        return self

    def get_profit_on_expiry(self, spot_price: float):
        net_profit = 0
        for order in self.option_orders:
            net_profit += order.get_profit_on_expiry(spot_price)
        return net_profit


if __name__ == '__main__':
    order1 = Order(Option(7800, Option.OptionType.CE, date.today()), Order.OrderType.Buy, 79)
    order2 = Order(Option(7900, Option.OptionType.CE, date.today()), Order.OrderType.Sell, 25)
    strategy1 = Strategy().add_order(order1).add_order(order2)
    print(strategy1)
    net_profit = strategy1.get_profit_on_expiry(7900)
    print(net_profit)
