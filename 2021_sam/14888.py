
def cal(opers, val, n):
	if max(opers)==0:
		if number[0] < val :
			number[0] = val
		if number[1] > val :
			number[1] = val
		return 
	for i, oper in enumerate(opers):
		if oper > 0 :
			if i==0:
				opers[i]-=1
				cal(opers, val+num_array[n], n+1)
			elif i==1:
				opers[i]-=1
				cal(opers, val-num_array[n], n+1)
			elif i==2:
				opers[i]-=1
				cal(opers, val*num_array[n], n+1)
			elif i==3:
				opers[i]-=1
				if val < 0 : 
					cal(opers, -int(abs(val)/num_array[n]), n+1)
				else : 
					cal(opers, int(val/num_array[n]), n+1)
			opers[i]+=1

	
n = int(input())
num_array = list(map(int, input().split()))
operators = list(map(int, input().split()))
number = [-int(1e9), int(1e9)]
if max(operators)==0 :
	number[0] = max(num_array)
	number[1] = min(num_array)
else : 
	cal(operators, num_array[0], 1)
print(number[0])
print(number[1])