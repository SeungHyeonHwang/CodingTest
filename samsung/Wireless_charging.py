




def batterCal(A,userA,userB):
	bcA = [0]*A
	bcB = [0]*A
	result = 0
	for i,ap in enumerate(AP) :
		# 거리 안
		if abs(userA[0]-ap[1]+1) + abs(userA[1]-ap[0]+1) <= ap[2] :
			bcA[i] = ap[-1]
		if abs(userB[0]-ap[1]+1) + abs(userB[1]-ap[0]+1) <= ap[2] :
			bcB[i] = ap[-1]
	if A == 1:
		return max(bcA[0], bcB[0])
	for i in range(A):
		for j in range(A):
			if i!=j:
				result = max(result, bcA[i] + bcB[j])
	return result


def moveUser(path, user):
	nx = user[0]+dx[path]
	ny = user[1]+dy[path]
	if 0>nx or nx>10 or 0>ny or ny>10:
		return [user[0],user[1]]
	else :
		return [nx,ny]

def solution(M,A):

	# 초기
	userA = [0,0]
	userB = [9,9]

	answer = batterCal(A,userA,userB)

	# M번
	for i in range(M):

		userA = moveUser(pathA[i], userA)
		userB = moveUser(pathB[i], userB)
		answer += batterCal(A,userA,userB)

	return answer


dx = [0,-1,0,1,0]
dy = [0,0,1,0,-1]
M,A = map(int, input().split())
pathA = list(map(int, input().split()))
pathB = list(map(int, input().split()))
AP = []
for _ in range(A):
	AP.append(list(map(int, input().split())))

print(solution(M,A))