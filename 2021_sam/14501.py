"""
못풀었음 
"""
"""
# 퇴사일까지 n
n = int(input())

time_array = [] # 각 상담을 완료하는데 걸리는 시간
pay_array = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n+1) # 다이나믹 프로그래밍을 위한 1차원 dp 테이블 초기화
max_num = 0

# 상담기간 t, 받을수 있는 금액 p
for i in range(n):
    t, p = map(int, input().split())
    time_array.append(t)
    pay_array.append(p)

for i in range(n-1, -1, -1):
	
	time = time_array[i] + i
	print(time_array[i]+i, n)
	# 상담 기간 안에 끝나는 경우
	if time <= n:
		# 점화식에 맞게, 현재까지의 최고 이익 계산
		dp[i] = max(pay_array[i] + dp[time], max_num)
		print(i, pay_array[i] + dp[time], max_num)
		max_num = dp[i]
	# 상담 기간을 벗어나는 경우
	else:
		dp[i] = max_num
	print(i ,' : ',dp)
print(max_num)
"""



# 뒤에서 날짜 되는지만 체크하면서 수익만 따지면됨 
# 어렵다 ... 다시 풀자
n = int(input())
day_array = []
pay_array = []
for i in range(n):
	t,p = map(int, input().split())
	day_array.append(t)
	pay_array.append(p)

dp = [0]*(n+1)
max_num  = 0
for i in range(n-1, -1, -1) : 
	day = day_array[i]+i
	if day <= n :
		dp[i] = max(dp[day] + pay_array[i], max_num)
		max_num = dp[i]
	else :
		dp[i] = max_num
	print(dp)
print(max_num)
















