# In[] : https://programmers.co.kr/learn/courses/30/lessons/42576
# 완주하지 못한 선수 level 1 


def solution(participant, completion):
    answer = ''
   
    participant.sort()
    completion.sort()
    
    # print(participant)
    # print(completion)
    
    for i in range(len(participant)):
        if i == len(participant)-1 : 
            return participant[i]
        elif participant[i] == completion[i] :
            # print(participant[i], completion[i])
            pass
        else : 
            return participant[i]
    # return answer


participant = ['leo', 'kiki', 'eden']
completion = ['eden', 'kiki']

participant = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']	
completion = ['josipa', 'filipa', 'marina', 'nikola']

participant =['mislav', 'stanko', 'mislav', 'ana']
completion = ['stanko', 'ana', 'mislav']

print(solution(participant, completion))