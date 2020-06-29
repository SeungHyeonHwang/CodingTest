# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 14:52:30 2020

@author: USER
"""


# In[] : https://programmers.co.kr/learn/courses/30/lessons/42578
# 위장
# 못품

def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    print(cnt)
    answer = reduce(lambda x, y: x+y+x*y, cnt.values())
    
    return answer

colthes = [['crow_mask', 'face'], 
            ['blue_sunglasses', 'face'], 
            ['blue_sunglasses', 'eyewear'], 
            ['green_turban', 'eyewear'], 
            ['smoky_makeup', 'face']]


print(solution(colthes))

# In[]
