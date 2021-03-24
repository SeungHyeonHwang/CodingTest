"""
# 내 풀이
"""
answer = 0
def dfs(i,l,result,numbers,target):
	global answer 
	if i == l-1 :
		if result == target :
			answer+=1
			return
		else :
			return
	i+=1
	dfs(i,l,result + numbers[i],numbers,target)
	dfs(i,l,result - numbers[i],numbers,target)
	return 

def solution(numbers, target):
	global answer 
	dfs(0,len(numbers),numbers[0],numbers,target)
	dfs(0,len(numbers),-numbers[0],numbers,target)
	return answer
answer = 0
numbers = [1,1,1,1,1]
target = 3
print(solution(numbers, target))

