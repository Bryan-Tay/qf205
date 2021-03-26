from  trinomial import trinomial_tree

S = 100.00 # spot price
K = 101.00 # strike price
r = 0.04 # 6% risk free interest rate
q = 0 # 0 dividend yield
T = 1 # year, maturity, 365 days to exp
N = 3 # number of steps
t = T/N
sigma = 0.2

print(trinomial_tree(S, K, r, q, T, sigma, N))
#Ans = 8.86



