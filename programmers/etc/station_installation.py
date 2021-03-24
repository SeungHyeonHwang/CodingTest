def solution(n, stations, w):
    answer = 0

	# 시작 왼쪽 탐색 
    propaSize = w*2+1
    rightIdx = 0

    # 왼쪽 탐색
    for i in range(len(stations)) : 
        nleftIdx = stations[i]-w 
        nrightIdx = stations[i]+w
        restDist = nleftIdx - rightIdx-1
   
        if restDist > 0 :
            answer += (restDist//propaSize)+1  if restDist%propaSize !=0 else restDist//propaSize
   
        rightIdx = nrightIdx
  
        if rightIdx >= n:
            return answer
        
        if i == len(stations)-1:
            answer += ((n - rightIdx)//propaSize)+1 if (n - rightIdx)%propaSize !=0 else ((n - rightIdx)//propaSize)
            return answer


n = 11
stations = [4,11]
w = 1

print(solution(n, stations, w))