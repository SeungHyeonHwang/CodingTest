# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 12:29:25 2020

@author: USER
"""


# In[] : https://programmers.co.kr/learn/courses/30/lessons/42841
# 숫자야구
# 다시풀


import itertools

def check(inning, cand) : 
    st, ba = 0,0
    
    b_cand_inning = []
    b_cand = []
    
    for i in range(3) : 
        if inning[i] == cand[i] :
            st+=1
        else :
            b_cand_inning.append(inning[i])
            b_cand.append(cand[i])
            
    for num in b_cand_inning :
        if num in cand : 
            ba +=1
        
    return st, ba

def solution(baseball) : 
    answer = 0
    
    candidate = list(itertools.permutations([i for i in range(1,10)], 3))
    
    
    for inning in baseball : 
        cand_list = []

        for cand in candidate : 
        
            pred = [int(i) for i in str(inning[0])]    
            if check(pred, cand) == (inning[1], inning[2]) : 
                cand_list.append(cand)
        candidate = cand_list
    answer = len(candidate)
    return answer 





baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]	
print(solution(baseball))



# In[]






