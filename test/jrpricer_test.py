from base.AmericanOption import AmericanOption
from base.EuropeanOption import EuropeanOption
from pricer.JrPricier import JrPricer

def test_jrpricer():

    AC = AmericanOption(100, 365, "C", 0)
    AP = AmericanOption(100, 365, "P", 0)

    EC = EuropeanOption(100, 365, "C", 0)
    EP = EuropeanOption(100, 365, "P", 0)

    JR = JrPricer(1000)

    assert abs(JR.pricing(AC, 100, 0.3, 0.01, 0 ) - 12.3683) < 0.0001
    assert abs(JR.pricing(AP, 100, 0.3, 0.01, 0 ) - 11.4477) < 0.0001

    assert abs(JR.pricing(EC, 100, 0.3, 0.01, 0 ) - 12.3683) < 0.0001
    assert abs(JR.pricing(EP, 100, 0.3, 0.01, 0 ) - 11.3733) < 0.0001



if __name__ == '__main__':
    test_jrpricer()
