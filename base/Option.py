from base.FinancialObject import FinancialObject

class Option(FinancialObject):

    def __init__(self, strike, maturity, type, start_date):
        if type != "C" and type != "P":
            raise TypeError('Option type must be C or P')
        if maturity < 0:
            raise TypeError('Maturity must be larger than 0')
        self.__strike = strike
        self.__maturity = maturity
        self.__type = type
        self.__start_date = start_date

    def get_strike(self):
        return self.__strike

    def get_maturity(self):
        return self.__maturity

    def get_type(self):
        return self.__type

    def get_start_date(self):
        return self.__get_start_date

    def get_payoff(self, price):
        if self.__type == "C":
            return max( 0.0 , price - self.__strike)
        elif self.__type == "P":
            return max( 0.0 , self.__strike - price)
        else:
            assert False

    def set_strike(self, strike):
        self.__strike = strike

    def set_strike(self, maturity):
        self.__maturity = maturity

    def set_type(self, type):
        self.__type = type

    def set_start_date(self, start_date):
        self.__start_date = start_date

    def is_callable(self, date):
        pass

    def is_effective(self, date):
        return date >= self.__start_date and date <= self.__maturity

    def is_option(self):
        return True
