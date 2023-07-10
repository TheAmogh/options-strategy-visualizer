from datetime import date
from enum import Enum

from option import Option


class Order:
    class OrderType(Enum):
        UNDEFINED = 0
        Buy = 1
        Sell = 2

    option = None
    order_type = None
    premium = None

    def __init__(self, option: Option, order_type: OrderType, premium: float):
        self.option = option
        self.order_type = order_type
        self.premium = premium

    def __repr__(self):
        return f"{self.option} {self.order_type.name} {self.premium}"

    def get_profit_on_expiry(self, spot_price: float):
        match self.order_type:
            case Order.OrderType.Buy:
                return self.option.get_intrinsic_value(spot_price) - self.premium
            case Order.OrderType.Sell:
                return self.premium - self.option.get_intrinsic_value(spot_price)
            case _:
                raise ValueError("Incorrect order type")


if __name__ == '__main__':
    order1 = Order(Option(2050, Option.OptionType.CE, date.today()), Order.OrderType.Buy, 6.35)
    print(order1)
    profit = order1.get_profit_on_expiry(2055)
    print(profit)
