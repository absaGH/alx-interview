#!/usr/bin/python3
'''
calculates the number of coins needed to meet a
given amount of total.
'''


def makeChange(coins, total):
    '''
    A function that reuturn the fewest number
    of coins.
    '''
    sum = 0
    count = 0
    if (total < 0):
        return -1
    for i in range(0, len(coins)):
        val = max(coins)
        while (sum < total):
            sum = sum + val
            if(sum <= total):
                count += 1
            else:
                sum = sum - val
                indx = coins.index(val)
                coins[indx] = 0
                break

    if(sum == total):
        return count
    else:
        return -1
