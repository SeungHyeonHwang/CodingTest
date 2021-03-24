# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 16:07:08 2020

@author: USER
"""


# In[] : https://programmers.co.kr/learn/courses/30/lessons/64065
# 튜플

def solution(s):
    answer = []

    s = s[2:-2]
    s = s.replace(',',' ')
    s = s.replace('{','')
    s = s.replace('}','a')

    
    chunk = []
    s_list = s.split('a')

    for w in s_list :
        chunk.append(list(map(int, w.strip().split())))
    chunk.sort(key = len)    
    start_s = chunk.pop(0)
    answer = start_s
    for l in chunk :
        next_s = list(set(l) - set(start_s))  
        start_s = l
        answer += next_s
    
    return answer


s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s = "{{123}}"
s = "{{20,111},{111}}"
s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"

print(solution(s))
