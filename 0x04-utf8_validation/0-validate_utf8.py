#!/usr/bin/python3
'''
Module to validate UTF-8
'''


def validUTF8(data):
    '''
    Implementation of UTF-8 validation algorithm
    '''
    size = len(data)
    counter = 0
    i = 0
    j = 0
    flag = True

    while i < size:
        if flag:
            s = bin(data[i])
            s = s.replace('0b', '')
            if not len(s) <= 7:
                while j < len(s):
                    if s[j] == '1':
                        counter += 1
                        j += 1
                    else:
                        break
                if counter != 0:
                    k = i + 1
                    while k < counter:
                        s = bin(data[k])
                        s = s.replace('0b', '')
                        if s[0] == '1' and s[1] == '0':
                            k += 1
                        else:
                            k = counter
                            flag = False
            i += 1
            counter = 0
        else:
            break

    return flag
