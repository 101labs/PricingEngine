from base.Option import Option

class EuropeanOption (Option):

    def __init__(self, strike, maturity, type, start_date):
        super().__init__(strike, maturity, type, start_date)

    def is_callable(self, date):
        if date > self.__start_date and date == self.__startdate + self.__maturity :
            return True
        else :
            return False

    def get_zone(self):
        return "E"
