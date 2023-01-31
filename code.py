def stockmax(prices):
    m = prices.index(max(prices))
    if m == len(prices)-1:
        r = (-1)*sum(prices[:m])+prices[m]*(len(prices)-1)
    elif m == 0:     
        r = stockmax(prices[m+1:])
    else:
        r = (stockmax(prices[:m+1])) + ( stockmax(prices[m+1:]) )
    return r

