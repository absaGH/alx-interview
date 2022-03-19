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


def delete_numbers(n, nums):
    """ delete numbers """
    for i in range(len(nums)):
        if nums[i] % n == 0:
            nums[i] = 0


def isWinner(x, nums):
    '''
    Function that implements prime game.
    It retruns the player with the most win.
    '''
    nums.sort()
    winner = False
    Maria = 0
    Ben = 0
    for game in range(x):

        nums2 = list(range(1, nums[game] + 1))

        turn = 0
        while True:
            change = False
            for i, n in enumerate(nums2):

                if n > 1 and isprime(n):
                    delete_numbers(n, nums2)
                    change = True
                    turn += 1
                    break

            if change is False:
                break
        if turn % 2 != 0:
            Maria += 1
        else:
            Ben += 1

    if Maria == Ben:
        return None
    if Maria > Ben:
        return "Maria"
    return "Ben"
