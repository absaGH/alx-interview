#!/usr/bin/python3
'''
Module to validate UTF8
'''


def validUTF8(data):
    '''
    Implementation of UTF8 validation algorithm
    '''
    size = len(data)
    counter = 0
    i = 0
    j = 0
    m = 0
    flag = True

    if size == 0:
        return flag
    while i < size:
        if flag:
            s = bin(data[i])
            s = s.replace('0b', '')
            if not len(s) <= 7:
                if len(s) > 8:
                    s = s[-8:]
                while j < len(s):
                    if s[j] == '1':
                        counter += 1
                        j += 1
                    else:
                        break
                if counter != 0 and counter <= 4:
                    k = i + 1
                    while m < counter - 1 and k < size:
                        s = bin(data[k])
                        s = s.replace('0b', '')
                        if len(s) == 8 and s[0] == '1' and s[1] == '0':
                            k += 1
                            m += 1
                        else:
                            m = counter
                            flag = False
                            break
                    if m < counter - 1:
                        return False
                else:
                    flag = False
                    break
            i += 1
            counter = 0
            j = 0
            m = 0
        else:
            break

    return flag
