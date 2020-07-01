# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 12:29:25 2020

@author: USER
"""


# In[] : https://programmers.co.kr/learn/courses/30/lessons/42841
# 숫자야구


# def dfs(i) : 
#     n,s,b = baseball
    
    

import itertools 
def solution(baseball):
    answer = 0 
    
    baseball = sorted(baseball, key=lambda x : (x[1], x[2]), reverse=True)
    
    for n,s,b in baseball : 
        
    
    return answer


baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]	
print(solution(baseball))

# In[]


def st_B(given, chosen):
    st = 0
    B = 0
    chosen_dif = []
    given_dif = []
    for i in range(3):
        if given[i] == chosen[i]:
            st += 1
        else:
            given_dif.append(given[i])
            chosen_dif.append(chosen[i])
    for num in chosen_dif:
        if num in given_dif:
            B += 1
    return st, B

import itertools

def solution(baseball):
    first = list(itertools.permutations([1,2,3,4,5,6,7,8,9], 3))
    second = []
    for each in baseball:
        given = [int(i) for i in str(each[0])]
        print(given)
        stb = (each[1], each[2])
        for chosen in first:
            if st_B(given, chosen) == stb:
                second.append(chosen)
        first = second
        second = []
    return len(first)

baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]	
print(solution(baseball))

# In[]

