#!/usr/bin/python3
'''
It is a game played by two players by removing
prime numbers from list.
'''


def isprime(num):
    '''
    Tests whether num is prime number or not.
    '''
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num < 2:
        return False
    for n in range(3, int(num**1 / 2) + 1, 2):
        if num % n == 0:
            return False
    return True


def isWinner(x, nums):
    '''
    Function that implements prime game.
    It retruns the player with the most win.
    '''
    count = 1
    noprime = True
    currentPlayer = 'Maria'
    resultdict = {'Maria': 0, 'Ben': 0}
    removed = []
    rmv = False
    if (x < 1):
        return None
    for round in nums:
        a_list = list(range(1, round + 1))
        currentPlayer = 'Maria'
        for val in a_list:

            rmv = False

            if(isprime(val)):
                for n in a_list:

                    if (n % val == 0 and not(n in removed)):

                        removed.append(n)
                        rmv = True
                if(currentPlayer == 'Maria'):
                    currentPlayer = 'Ben'
                else:
                    currentPlayer = 'Maria'
        if (not(rmv)):
            if(currentPlayer == 'Maria'):
                resultdict['Ben'] += 1
            else:
                resultdict['Maria'] += 1
        a_list.clear()
        removed.clear()
    return max(resultdict, key=resultdict.get)
