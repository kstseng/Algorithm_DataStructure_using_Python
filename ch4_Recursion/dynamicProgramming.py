def recMC(coinValueList, change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change - i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins

#print(recMC([1, 5, 10, 25], 26))

def dpMC(coinValueList, change, minCoins):
    for cents in range(change + 1):
        coinCount = cents
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
        minCoins[cents] = coinCount
    return minCoins, minCoins[change]

change = 63
minCoinsList, minCoins =  dpMC([1, 5, 10, 21, 25], change, [0]*(change + 1))
print('number of coins: {}'.format(minCoins))


