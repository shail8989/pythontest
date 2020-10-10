def buyLotsOfFruit(orderList):
    """
        orderList: List of (fruit, numPounds) tuples

    Returns cost of order
    """
    totalCost = 0.0
    
    for f, q in orderList:
        totalCost += fruitPrices[f] * q
    "* YOUR CODE HERE *"
    return totalCost