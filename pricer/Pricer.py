class Pricer:

    def __init__(self):
        pass

    def pricing(self, object, underlying_price):
        if not object.is_FinancialObject():
            raise TypeError('pricer can only pricing financial_object')
        pass
