# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 15:06:05 2020

@author: USER
"""


# In[] : https://programmers.co.kr/learn/courses/30/lessons/42839
# 소수찾기


import itertools 

def solution(numbers):
    answer = 0
    dicts = {}
    for i in range(len(numbers)) : 
        for com in itertools.permutations(numbers, i+1) : 
            
            number = int(''.join(list(com)))
            if number not in dicts and number > 1: 
                dicts[number] = number
                for j in range(2, number) :
                    if number%j == 0 :
                        break
                else :
                    answer +=1
    return answer


numbers = "17"
numbers = "011"
numbers = "012345"

print(solution(numbers))
# In[]

