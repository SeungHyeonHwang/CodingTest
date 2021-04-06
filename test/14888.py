
def cal(i,n1,n2):
	if i==0 : n1+=n2
	elif i==1 : n1-=n2
	elif i==2 : n1*=n2
	else :
		if n1 < 0 and n2 > 0: n1=-(abs(n1)//n2)
		else : n1=n1//n2
	return max(min(int(1e9), n1), -int(1e9)) 


def dfs(i, num, oper, result):
	global minValue, maxValue
	if not num:
		maxValue = max(result, maxValue)
		minValue = min(result, minValue)
		return
	for i in range(4):
		if oper[i] > 0 :
			oper[i]-=1
			dfs(i, num[1:], oper,  cal(i, result, num[0]))
			oper[i]+=1

def solve():
	for i in range(4):
		if operator[i] > 0 :
			operator[i]-=1
			dfs(i, a[2:], operator, cal(i, a[0], a[1]))
			operator[i]+=1

maxValue=-int(1e9)
minValue=int(1e9)
n = int(input())
a = list(map(int, input().split()))
operator = list(map(int, input().split()))
solve()
print(maxValue)
print(minValue)