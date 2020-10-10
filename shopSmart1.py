def shopSmart(orderList, fruitShops):
    """
        orderList: List of (fruit, numPound) tuples
        fruitShops: List of FruitShops
    """
    "* YOUR CODE HERE *"
    priceOfOrderDict = { 'shop1': shops[0].getPriceOfOrder(orderList), 'shop2': shops[1].getPriceOfOrder(orderList)}
    shopsDict = {'shop1': fruitShops[0], 'shop2': fruitShops[1]}
    
    temp = min(priceOfOrderDict.values()) 
    res = [key for key in priceOfOrderDict if priceOfOrderDict[key] == temp]
    res = str(res[0])
    res = shopsDict[res]
    
    return res