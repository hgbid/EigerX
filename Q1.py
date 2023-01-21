"""
the function gets a number and return the sum of it's digits
"""

WRONG_INPUT = -1


def checkInput(products, productPrices, productSold, soldPrice):
    if len(products) != len(productPrices) or len(productSold) != len(soldPrice):
        return WRONG_INPUT


def priceCheck(products, productPrices, productSold, soldPrice):
    if checkInput(products, productPrices, productSold, soldPrice) == WRONG_INPUT:
        return WRONG_INPUT

    prod_prices_dic = {}
    for index in range(len(products)):
        prod_prices_dic[products[index]] = productPrices[index]

    errors = 0
    for index in range(len(productSold)):
        if prod_prices_dic[productSold[index]] != soldPrice[index]:
            errors += 1
    return errors


if __name__ == '__main__':
    errors_amount = priceCheck(products=['rice', 'sugar', 'wheat', 'cheese'],
                               productPrices=[16.89, 56.92, 20.89, 345.99],
                               productSold=['rice', 'cheese'],
                               soldPrice=[18.99, 400.89])
    print(errors_amount)
