from base.Option import Option

class AmericanOption (Option):

    def __init__(self, strike, maturity, type):
        super().__init__(strike, maturity, type)

    def is_callable(self, date):
        if date > self.__start_date and date <= self.__startdate + self.__maturity :
            return True
        else :
            return False
