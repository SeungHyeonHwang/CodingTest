# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 14:50:21 2020

@author: USER
"""


# In[] : https://programmers.co.kr/learn/courses/30/lessons/42579
# 베스트앨범
# dictionary, tuple, sort, lambda 

def solution(genres, plays):
    answer = []
    
    dicts = {}
    
    for i in range(len(genres)) : 
        if genres[i] in dicts : 
            dicts[genres[i]].append((i, plays[i]))
        else : 

            dicts.setdefault(genres[i], [(i, plays[i])])
    best = {}

    for i, key in enumerate(dicts) :
        sums = 0
        for song in dicts[key] : 
            sums += song[1]
        best[key] = sums
        
    best = (sorted(best.items(), key=lambda x : x[1], reverse=True))

    for key in best : 
        for i,ans in enumerate(sorted(dicts[key[0]], key=lambda x : (-x[1], x[0]))) :
            answer.append(ans[0])
            if i == 1:
                break
    return answer



genres = ['classic', 'pop', 'classic']
plays = [500, 600, 150]
print(solution(genres, plays))

# In[]