import numpy as np

def getBondPrice(y, face, couponRate, m, ppy):
    efr=y/ppy
    ccf=couponRate*face/ppy
    
    if ppy==1:
      times=np.arange(1,m+1)
    else:
      times=np.arange(1,ppy*m+1)
    pvf=np.power(1+efr, times)
    pvcf=ccf/pvf
    pvface=face/pvf[-1]
    BondPrice=pvface+pvcf.sum()

    return BondPrice
