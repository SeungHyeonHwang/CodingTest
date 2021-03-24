# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 14:51:44 2020

@author: USER
"""


# In[] : https://programmers.co.kr/learn/courses/30/lessons/42840
# 완전탐색 
# 모의고사

def solution(answers):
    answer = []
    people = [[] for _ in range(3)] 
    max_n = 1e5
    people_ans = [0 for _ in range(3)]
    people[0] = ([1,2,3,4,5]*int(max_n//5))
    people[1] = ([2, 1, 2, 3, 2, 4, 2, 5]*int(max_n//8))
    people[2] = ([3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*int(max_n//10))
    
    for i, person in enumerate(people) : 
        for j in range(len(answers)) : 

            if person[j] == answers[j] :
                people_ans[i] += 1

    max_n = max(people_ans)
    for i in range(3) : 
        if max_n == people_ans[i] : 
            answer.append(i+1)
    return answer

answers = [1,2,3,4,5]
# answers = [1,3,2,4,2]

print(solution(answers))


# In[]

# 다른사람 풀이 1


def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result


# In[] : 
# 다른사람 풀이 2
from itertools import cycle

def solution(answers):
    giveups = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]

