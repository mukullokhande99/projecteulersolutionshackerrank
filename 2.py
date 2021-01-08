#!/bin/python3

num =int(input())
for i in range(num):
    a= int(input())
    p =[1, 2];
    r =2
    while(p[-1]+p[-2]<=a):
        p.append(p[-2]+p[-1])
        if(p[-1]%2 == 0):
            r+=p[-1];
    print(r)
    