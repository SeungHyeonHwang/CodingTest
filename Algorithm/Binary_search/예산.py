


# In[] : https://programmers.co.kr/learn/courses/30/lessons/43237
# 예산
# ver.1 

def solution(budgets, M):
    budgets.sort()
    l = len(budgets)
    cap = 0
    for i, budget in enumerate(budgets):
        level = (budget - cap) * (l - i)
        if level <= M:
            cap = budget
            M -= level
        else:
            cap += M // (l - i)
            break
    return cap


budgets = [120, 110, 140, 150]
M = 485 
print(solution(budgets, M))



# In[] : ver.2
    
    
def solution(budgets, M):
    if sum(budgets) <= M:
        return max(budgets)

    l, r, mid = 1, max(budgets), 0
    answer = 0

    while l <= r:
        mid = (l+r) // 2
        total = 0
        print(mid, l, r)
        for budget in budgets:
            if budget <= mid:
                total += budget
            else:
                total += mid

        if total > M:
            r = mid - 1
        else:
            if answer <= mid:
                answer = mid
            l = mid + 1
    return answer    



budgets = [120, 110, 140, 150]
M = 485 
print(solution(budgets, M))

  
# In[] : ver.3 

def solution(budgets, M) : 
    
    l,r,mid = 0, max(budgets), 0
    answer = 0 
    
    while l <= r :
        mid = (l+r)//2
        print(mid)
        total = 0 
        for budget in budgets : 
            if budget > mid : 
                total += mid
            else :
                total += budget
        if total <= M :
            if answer <= mid :
                answer = mid
            l = mid + 1
        else : 
            r = mid - 1
            
    return answer 
            
            
            

budgets = [120, 110, 140, 150]
M = 485 
print(solution(budgets, M))