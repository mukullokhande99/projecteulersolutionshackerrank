#!/bin/python3
import sys

arr = int(input().strip())
for i in range(arr):
    num = int(input().strip())
    total_sum = 0
    p = 0
    q = 1
    while q < num:
        if q%2==0:    #even
            total_sum += q
        p,q = q,p+q
    print(total_sum)
    