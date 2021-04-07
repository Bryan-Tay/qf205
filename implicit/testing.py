'''
S, K, r, q, T, sigma, M, N, call
𝑺 = current price, spot price
𝑲 = exercise price, strike price
𝒓 = risk-free rate, Risk-Free Interest Rate
𝒒 = dividends, Dividend Yield 
𝑻 = time to expiration, maturity 
v, 𝝈, sigma = volatility
M = the price now
𝑵 = number of steps, 
    N can be default to 1

def Implicit(S, K, r, q, T, sigma, M, N, call):
'''
from implicit_formula import *

S = 80
K= 100
r= 0.05
q = 0
# The blue line have the risk free interest rate r = 0:05, 
# the red line r = 0:075 and the yellow line r = 0:1.
T= 1
sigma= 0.2
M = 2000  # Unsure
N = 2000  # Unsure
call=1

print(Implicit(S, K, r, q, T, sigma, M, N, call))
# expected 1.8599