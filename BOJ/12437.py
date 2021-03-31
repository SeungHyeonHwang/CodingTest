


# 3 11 4

def solution(cal):
    answer = 0
    start = 0 

    for i in range(cal[0]):
        end = (cal[1]+start)%cal[2]
        answer+=(cal[1]+start)//cal[2]
        if end == 0 :
            start = 0
        elif end != 0 : 
            answer+=1
            start = end

    return answer 


t = int(input())

callendar = [list(map(int, input().split())) for _ in range(t)]

for i,cal in enumerate(callendar) :
    print('Case #%d: %d'%(i+1, solution(cal)))