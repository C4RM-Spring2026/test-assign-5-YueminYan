import numpy as np

def getBondDuration(y, face, couponRate, m, ppy = 1):
    ccf=couponRate*face/ppy
    times=np.arange(1,m+1)
    pvf=np.power(1+y, times)
    pvcf=ccf/pvf
    pvface=face/pvf[-1]
    BondPrice=pvface+pvcf.sum()
    d1=pvcf*times
    d2=pvface*m
    Duration=(np.sum(d1)+d2)/BondPrice
    return Duration
