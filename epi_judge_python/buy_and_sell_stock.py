from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    # TODO - you fill in here.
    min_price, max_profit = float('inf'), 0.0

    for price in prices:
        if price < min_price:
            min_price = price
        
        temp_profit = price-min_price

        if temp_profit > max_profit:
            max_profit = temp_profit

    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
