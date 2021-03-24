import pandas as pd
import copy
import numpy as np
import math

def trinomial_tree(S, K, r, q, t, T, sigma, N):

    u = np.exp(sigma*math.sqrt(3 * t))
    d = 1/u
    pu = np.sqrt( ( t / (12* sigma**2) )) * (r -  ( (sigma**2)/2) ) + 1/6 
    pd = - np.sqrt( ( t / (12 * sigma**2) )) * (r - ( (sigma**2)/2) ) + 1/6
    pm = 2/3

    # initialising the array with spot price
    array_a = [S] 

    for i in range(N): 
        # initializing the first array
        temp = array_a[0] * u # insert at front
        array_a.insert(0, temp)
        temp = array_a[-1] * d # append to back
        array_a.append(temp)

    # Initialize first array for call prices
    call_prices = [max(x - K, 0) for x in array_a] # cannot fall below 0

    array2 = call_prices[:] #copy call prices array
    
    for i in range(N):
        temp = []
        if len(array2) > 2:
            for i in range(len(array2)-2):
                value1 = array2[i]
                value2 = array2[i+1]
                value3 = array2[i+2]

                value = np.exp(-r * t) * (value1 * pu + value2 * pm + value3 * pd)
                temp.append(value)

            array2 = temp

            
    return(round(array2[0],2))