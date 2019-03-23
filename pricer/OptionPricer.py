from pricer.Pricer import Pricer

class OptionPricer(Pricer):
    def __init__(self):
        super().__init__()

    def pricing(self, option, underlying_price):
        super().pricing(option, underlying_price)
        if not option.is_option():
            raise TypeError("This pricer can only be applied on option")
        pass
