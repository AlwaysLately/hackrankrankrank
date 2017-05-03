
import sys

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
number = raw_input().strip()


number = map(lambda x: int(x), list(number))
change = 0
flag = 0
has_changed_checker = []

i = 0
for i in xrange(n / 2):
    if number[i] != number[n - i - 1]:
        has_changed_checker.append(i)
        if number[i] > number[n - i - 1]:
            number[n - i - 1] = number[i]
        else:
            number[i] = number[n - i - 1]
        change += 1

if change > k:
    print -1
    flag = 1

if flag == 0:
    i = 0
    for i in xrange(n / 2):
        if i in has_changed_checker:
            if number[i] != 9 and change  < k:
                change += 1
                number[i] = 9
                number[n - i - 1] = 9
        elif number[i] != 9 and change + 1 < k:
            change += 2
            number[i] = 9
            number[n - i - 1] = 9

    if n % 2 != 0 and k - change > 0:
        number[n / 2] = 9
    result = [str(j) for j in number]
    print int(''.join(result))
# number = map(lambda x: int(x), list(number))
# flag = 0
# change = 0

# for i in xrange(n / 2):
#     if number[i] != number[n - i - 1]:
#         change += 1
# if change > k:
#     print -1
#     flag = 1
#     break
# else:
#     i = 0
#     for i in xrange(n / 2):
#         if k < 0:
#             print -1
#             flag = 1
#             break
#         else:
#             if number[i] == number[n - i - 1] and number[i] != 9:
#                 k -= 2
#                 if k < 0:
#                     k += 2
#                 else:
#                     number[i] = 9
#                     number[n - i - 1] = 9
#             elif number[i] == number[n - i - 1] and number[i] == 9:
#                 pass
#             elif number[i] != number[n - i - 1] and 9 in (number[i], number[n - i - 1]):
#                 k -= 1
#                 if k < 0:
#                     print -1
#                     flag = 1
#                     break
#                 else:
#                     number[i] = 9
#                     number[n - i - 1] = 9
#             else:
#                 k -= 2
#                 if k < 0:
#                     k += 2
#                     k -= 1
#                     if k < 0:
#                         print -1
#                         flag = 1
#                         break
#                     else:
#                         if number[i] > number[n - i - 1]:
#                             number[n - i - 1] = number[i]
#                         else:
#                             number[i] = number[n - i - 1]
#                 else:
#                     number[i] = 9
#                     number[n - i - 1] = 9


# if n % 2 == 0:
#     pass
# else:
#     if k > 0 and number[n / 2] != 9:
#         number[n / 2] = 9

# if flag == 0:
#     result = [str(j) for j in number]
#     print int(''.join(result))
