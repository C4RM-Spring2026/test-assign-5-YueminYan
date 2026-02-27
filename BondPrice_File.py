import numpy as np

def getBondPrice(y, face, couponRate, m, ppy):
    ccf=couponRate*face/ppy
    times=np.arange(1,m+1)
    pvf=np.power(1+y, times)
    pvcf=ccf/pvf
    pvface=face/pvf[-1]
    BondPrice=pvface+pvcf.sum()
    return BondPrice
