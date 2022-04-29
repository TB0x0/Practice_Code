#!/usr/bin/python
import sys

def shortCondorCalc(atm_straddle_price, current_ticker_price):
    strikes = []
    ctp = float(current_ticker_price)
    asp = float(atm_straddle_price)
    risk_delta = ctp * .02
    short_put = ctp - asp
    short_call = ctp + asp
    long_put = short_put - risk_delta
    long_call = short_call + risk_delta

    strikes.append("Calculated risk delta: {:.2f}\n ".format(risk_delta))
    strikes.append("Long Put: {:.2f}\n".format(long_put))
    strikes.append("Short Put: {:.2f}\n".format(short_put))
    strikes.append("Short Call: {:.2f}\n".format(short_call))
    strikes.append("Long Call: {:.2f}\n".format(long_call))

    return strikes
