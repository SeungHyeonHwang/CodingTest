# filter 를 list.count(0) 로 바꿨더니 시간초과 해결...



from collections import deque

n,k = map(int, input().split())
durability = list(map(int, input().split()))

robots = [0]*n
ans = 0
while True: 
	ans+=1
	# 같이 회전
	last = durability.pop()
	durability.insert(0,last)
	last = robots.pop()
	robots.insert(0,last)
	

	# 먼저 올라간 로봇부터 하기 
	robots[n-1] = 0
	for i in range(len(robots)-2,-1,-1) : 

		if robots[i] > 0 and durability[i+1] >= 1 and robots[i+1] == 0 :
			if i == len(robots)-2 :
				robots[i] = 0 
			else : 
				robots[i] = 0
				robots[i+1] = 1
			durability[i+1]-=1

	if durability[0] > 0 :
		robots[0] = 1
		durability[0]-=1
	if durability.count(0) >=k :
		break
print(ans)

