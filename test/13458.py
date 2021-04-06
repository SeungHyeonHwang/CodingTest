

n = int(input())
answer=0
numbers = list(map(int, input().split()))
bc = list(map(int,input().split()))
for num in numbers:
	num-=bc[0]
	if num <= 0 :
		continue
	if num <= bc[1]:
		answer+=1
		continue
	else : 
		answer += int(num/bc[1])
		if num%bc[1] > 0 :
			answer+=1
print(answer+len(numbers))
