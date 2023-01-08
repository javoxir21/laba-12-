#!/usr/bin/env python3
# -*- coding: utf-8 -*-


new_set = [1,2,3,4]
power_set = [[]]
for x in new_set:
    new_set = power_set
    for i in range(len(new_set)):
        new_set[i].append(x)
    power_set.extend(new_set)
print(power_set)
