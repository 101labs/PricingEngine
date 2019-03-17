class Option:

    def __init__(self, strike, maturity, type, start_date):
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
