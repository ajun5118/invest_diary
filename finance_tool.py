import math

from collections import abc

import numbers

def pv(rate,nper,amt):
    return amt * math.pow((1 + rate),-nper)

def npv(rate,cash_flw,verbose = False):
    if isinstance(cash_flw,abc.Sequence):
        
        result = []
        for item,value in enumerate(cash_flw,start = 1):
            result.append(value * math.pow((1 + rate),-item))
        if not verbose:
            result = sum(result)
    else:
        raise TypeError('cash_flw is not Sequence')
    return result

def fv(rate,nper,amt):
    
    return  amt * math.pow((1+rate),nper)

def nfv(rate,cash_flw,verbose = False):
    if isinstance(cash_flw,abc.Sequence):
        n = reversed(range(1,len(cash_flw) + 1))
        
        result = []
        for item,value in zip(n,cash_flw):
            result.append(value * math.pow((1 + rate),item))
        if not verbose:
            result = sum(result)
    else:
        raise TypeError('cash_flw is not Sequence')
    return result