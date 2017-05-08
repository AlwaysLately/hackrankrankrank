#!/usr/bin/env python
# -*- coding: utf-8 -*-


n = int(raw_input())
s = raw_input()
reved_s = s[::-1]
each_count = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
fst_index = 0
lst_index = 0

for i in xrange(n):
    each_count[s[i]] += 1
    if each_count[s[i]] > n / 4:
        fst_index = i
        break
i = 0
each_count = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
for i in xrange(n):
    each_count[reved_s[i]] += 1
    if each_count[reved_s[i]] > n / 4:
        lst_index = i
        break
print n - lst_index - fst_index
