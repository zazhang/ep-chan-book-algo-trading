#!usr/bin/env ipython

"""Hurst Exponent
https://www.quantstart.com/articles/Basics-of-Statistical-Mean-Reversion-Testing
https://stackoverflow.com/questions/39488806/hurst-exponent-in-python
"""

from numpy import log, polyfit, var, subtract


def hurst_ernie_chan(p, lag_range=None):

    p_log = log10(p) # use log price

    variancetau = []
    tau = []
    
    # Create the range of lag values
    if lag_range == None:
        lags = [2]
    else:
        lags = range(2, lag_range) # lag_range < len(ts)

    for lag in lags: 

        #  Write the different lags into a vector to compute a set of tau or lags
        tau.append(lag)

        # call this pp or the price difference
        pp = subtract(p_log[lag:], p_log[:-lag])
        variancetau.append(var(pp))

    # we now have a set of tau or lags and a corresponding set of variances
    #print tau
    #print variancetau

    # plot the log of those variance against the log of tau and get the slope
    m = polyfit(log10(tau),log10(variancetau),1)

    hurst = m[0] / 2

    return hurst