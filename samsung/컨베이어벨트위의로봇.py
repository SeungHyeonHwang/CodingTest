
import copy
def runConveyor(arr):
	cnt = 0
	arr = copy.deepcopy(arr)
	arr.sort()
	for i in range(len(arr)):
		if arr[i] > 0 :
			return True
		elif arr[i] == 0 :
			cnt+=1
			if cnt >= K :
				return False
	return True

def moveRobot(pos):
	
	if an[pos+1] > 0 and not robot[pos+1] : 
		an[pos+1]-=1
		robot[pos] = 0 
		robot[pos+1] = 1 
		return pos+1
	else : 
		return None

def conveyor():
	global answer 

	i = 0
	while True : 

		# 1.벨트 이동
		end = an.pop()
		an.insert(0, end)
		end = robot.pop()
		robot.insert(0, 0)
		robot[N-1] = 0

		# 먼저 올라간 로봇부터
		for j in range(len(robot)-2, -1, -1) : 
			if robot[j] : 
				# 2.1 로봇 이동하는지 여부 체크
				
				pos = moveRobot(j)
				# 로봇 이동하지 않으면 
				if pos is None :
					break

		# N 위치 로봇은 무조건 내려감
		robot[N-1] = 0

		# 1번에 로봇 올림
		if an[0] > 0 and not robot[0] :
			an[0]-=1
			robot[0] = 1
	

		i+=1

		# 4. 내구도 조사
		result = runConveyor(an)
		if not result :
			break

	answer = i


#N, K = map(int, input().split())
#an = [list(map(int, input().split())) for _ in range(4)]

an = []
answer=0
my_file = open('ex4.txt')
for i, each_line in enumerate(my_file): 
	if i == 0: N, K = map(int, each_line.split())
	else : an =  list(map(int, each_line.split()))
robot = [0]*N
conveyor()
print(answer)