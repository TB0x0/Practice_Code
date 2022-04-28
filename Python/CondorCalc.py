#!/usr/bin/python
import sys

def shortCondorCalc(atm_straddle_price, current_ticker_price):
    ctp = float(current_ticker_price)
    asp = float(atm_straddle_price)
    risk_delta = ctp * .02
    short_put = ctp - asp
    short_call = ctp + asp
    long_put = short_put - risk_delta
    long_call = short_call + risk_delta

    print("Calculated risk delta: {:.2f}\n ".format(risk_delta))
    print("Long Put: {:.2f}\n".format(long_put))
    print("Short Put: {:.2f}\n".format(short_put))
    print("Short Call: {:.2f}\n".format(short_call))
    print("Long Call: {:.2f}\n".format(long_call))

if __name__ == '__main__':
    shortCondorCalc(sys.argv[1], sys.argv[2])
