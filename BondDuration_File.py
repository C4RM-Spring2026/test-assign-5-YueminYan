import numpy as np

def getBondDuration(y, face, couponRate, m, ppy):
  efr=y/ppy
  ccf=couponRate*face/ppy
  if ppy==1:
    times=np.arange(1,m+1)
  else:
    times=np.arange(1,2*m+1)
  pvf=np.power(1+efr, times)
  pvcf=ccf/pvf
  pvface=face/pvf[-1]
  BondPrice=pvface+pvcf.sum()
  if ppy==1:
    d1=pvcf*times
    d2=pvface*m
  else:
    times_d=times/ppy
    d1=pvcf*times_d
    d2=pvface*m
  Duration=(np.sum(d1)+d2)/BondPrice
  return Duration
