




n=int(input())
inArr = [input() for _ in range(n)]
outArr = [input() for _ in range(n)]
orders = {string:i for i,string in enumerate(inArr)}
answer = 0

# 현재 차량 순위
for i in range(n-1):
	# 내 뒤 차량 순위
	for j in range(i+1,n):
		# 현재가 크면 현재 차가 추월 한 것
		if orders[outArr[i]] > orders[outArr[j]] : 
			answer+=1
			break

print(answer)
