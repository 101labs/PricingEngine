import math
from pricer.OptionPricer import OptionPricer

class JrPricer(OptionPricer):

    def __init__(self, layer):
        if layer <= 0:
            raise TypeError('layer must be larger than 0')
        self.__layer=layer

    def pricing(self, option, underlying_price, sigma, rate, date):
        super().pricing(option, underlying_price)
        if not option.is_effective(date):
            return 0.0
        else:
            option_type= option.get_zone()
            period = (option.get_maturity() - date) / (365 * self.__layer) #to be changed, 365 is not accurate
            up_ratio = math.exp((rate - sigma * sigma * 0.5) * period + sigma * math.sqrt(period))
            down_ratio = math.exp((rate - sigma * sigma * 0.5) * period - sigma * math.sqrt(period))
            up_down_ratio = up_ratio / down_ratio

            prices = [None] * (self.__layer + 1)
            prices[0] = underlying_price * math.pow(down_ratio, self.__layer)
            for i in range (1,self.__layer+1): prices[i] = up_down_ratio * prices[i-1]

            values = [None] * (self.__layer + 1)
            for i in range (0,self.__layer+1):
                values[i] = option.get_payoff(prices[i])

            seq = range(0,self.__layer)
            for i in reversed(seq):
                for j in range(0,i+1):
                    if option_type == "E":
                        values[j] = (0.5 * values[j+1] + 0.5 * values[j]) * math.exp ( (0 - rate)* period)
                    elif option_type == "A":
                        values[j] = max( (0.5 * values[j+1] + 0.5 * values[j]) * math.exp ( (0 - rate)* period), option.get_payoff(prices[j] / math.pow(down_ratio, self.__layer - i)) )

            return values[0]
