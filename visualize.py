from datetime import date

import matplotlib.pyplot as plt
import numpy as np

from option import Option
from order import Order
from strategy import Strategy


class Visualize:
    strategy = None

    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def plot_payout_graph(self, low: float, high: float, datapoints: int = 1000):
        x = np.linspace(low, high, datapoints)
        y = np.vectorize(lambda spot_price: self.strategy.get_profit_on_expiry(spot_price))(x)
        self.plot_x_y(x, y)

    def plot_x_y(self, x, y):
        plt.plot(x, y)
        plt.plot(x, np.zeros(x.shape))
        plt.show()


if __name__ == '__main__':
    # Bull Call Spread
    order1 = Order(Option(7800, Option.OptionType.CE, date.today()), Order.OrderType.Buy, 79)
    order2 = Order(Option(7900, Option.OptionType.CE, date.today()), Order.OrderType.Sell, 25)
    call_ratio_back_spread = Strategy().add_order(order1).add_order(order2)
    print(call_ratio_back_spread)
    Visualize(call_ratio_back_spread).plot_payout_graph(7600, 8100)

    # Bull Put Spread
    order1 = Order(Option(7700, Option.OptionType.PE, date.today()), Order.OrderType.Buy, 72)
    order2 = Order(Option(7900, Option.OptionType.PE, date.today()), Order.OrderType.Sell, 163)
    long_straddle = Strategy().add_order(order1).add_order(order2)
    print(long_straddle)
    Visualize(long_straddle).plot_payout_graph(7500, 8100)

    # Call Ratio Back Spread
    order1 = Order(Option(7600, Option.OptionType.CE, date.today()), Order.OrderType.Sell, 201)
    order2 = Order(Option(7800, Option.OptionType.CE, date.today()), Order.OrderType.Buy, 78)
    order3 = Order(Option(7800, Option.OptionType.CE, date.today()), Order.OrderType.Buy, 78)
    call_ratio_back_spread = Strategy().add_order(order1).add_order(order2).add_order(order3)
    print(call_ratio_back_spread)
    Visualize(call_ratio_back_spread).plot_payout_graph(7400, 8300)

    # Long Straddle
    order1 = Order(Option(7600, Option.OptionType.CE, date.today()), Order.OrderType.Buy, 77)
    order2 = Order(Option(7600, Option.OptionType.PE, date.today()), Order.OrderType.Buy, 88)
    long_straddle = Strategy().add_order(order1).add_order(order2)
    print(long_straddle)
    Visualize(long_straddle).plot_payout_graph(7100, 8100)
