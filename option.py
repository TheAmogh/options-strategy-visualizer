from datetime import date
from enum import Enum


class Option:
    class OptionType(Enum):
        UNDEFINED = 0
        CE = 1
        PE = 2

    strike_price = None
    option_type = None
    expiry = None

    def __init__(self, strike_price: float, option_type: OptionType, expiry: date):
        self.strike_price = strike_price
        self.option_type = option_type
        self.expiry = expiry

    def __repr__(self):
        return f"{self.strike_price}{self.option_type.name}"

    def get_intrinsic_value(self, spot_price: float) -> float:
        match self.option_type:
            case Option.OptionType.CE:
                return max(0, spot_price - self.strike_price)
            case Option.OptionType.PE:
                return max(0, self.strike_price - spot_price)
            case _:
                raise ValueError("Incorrect option type")


if __name__ == '__main__':
    option1 = Option(15000, Option.OptionType.CE, date.today())
    print(option1)
    intrinsic_value = option1.get_intrinsic_value(15678.85)
    print(intrinsic_value)
