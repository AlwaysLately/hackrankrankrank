#!/bin/python

import sys


n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
number = raw_input().strip()

number = map(lambda x: int(x), list(number))
digit_not_equal = 0
digit_is_nine = 0
digit_change_into_nine = 0
for i in xrange(n / 2):
    if number[i] != number[n - 1 - i]:
        digit_not_equal += 1
        if number[i] == 9 or number[n - 1 - i] == 9:
            digit_is_nine += 1

if digit_not_equal > k:
    print -1
else:
    digit_both_changed = k - digit_not_equal
    sum_digit = 0
    for i in xrange(n / 2):
        if number[i] != number[n - 1 - i]:
            if sum_digit < digit_both_changed:
                number[i] = number[n - 1 - i] = 9
                sum_digit += 1
            else:
                number[i] = number[
                    n - 1 - i] = number[i] if number[i] > number[n - 1 - i] else number[n - 1 - i]

    result = [str(i) for i in number]
    print ''.join(result)
