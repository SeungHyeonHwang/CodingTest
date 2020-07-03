# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 16:14:52 2020

@author: USER
"""


# In[] : https://programmers.co.kr/learn/courses/30/lessons/64064
# 불량 사용자
# 못품

from itertools import product

def check(str1, str2):
    if len(str1) != len(str2): # 길이 다르면 False 
        return False
    for i in range(len(str1)): 
        if str1[i] == "*": # *는 무시
            continue
        if str1[i] != str2[i]: # 같지않으면 False
            return False
    return True # 통과하면 True

def solution(user_id, banned_id):
    answer = set()
    result = [[] for i in range(len(banned_id))]

    for i in range(len(banned_id)):
        for u in user_id:
            if check(banned_id[i], u):
                result[i].append(u)

    result = list(product(*result)) # 2개 이상 list에서 모든 조합 
    for r in result:
        if len(set(r)) == len(banned_id):
            answer.add("".join(sorted(set(r))))

    return len(answer)

    
    
user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]    
    
# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["*rodo", "*rodo", "******"]

# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["fr*d*", "*rodo", "******", "******"]

print(solution(user_id, banned_id))