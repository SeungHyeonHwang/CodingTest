
def check(p):


def play(i, p, result):
	if i > 9 : 
		answer.append(result)
		return

	for j in range(4):
		# 이미 도착한 말이면
		if p[j][1] == -1 :
			continue

		p[j][1]+=dices[i]

		# 길이 벗어나면 
		if p[j][1] >= len(board[p[j][0]]) :
			prev, p[j][1] = p[j][1],-1
			play(i+1, p, result) 
			p[j][1] = prev

		elif p[j][0] == 0 and p[j][1]%5 == 0 and p[j][1]!=20:
			play(i+1, p, result+board[p[j][1]//5][p[j][1]])
		else : 
			play(i+1, p, result+board[p[j][0]][p[j][1]])
		p[j][1]-=dices[i]

def solution(dices):
	play(0, [[0]*2 for _ in range(4)], 0)
	return max(answer)

answer = []
dices = list(map(int, input().split()))
lst1 = [i*2 for i in range(40)]
lst1.append(0)
end = [25, 30, 35, 40, 0]
lst2 = lst1[:6] + [13, 16, 19] + end
lst3 = lst1[:11] + [22, 24] + end
lst4 = lst1[:16] + [28, 27, 26] + end
board = [lst1, lst2, lst3, lst4]

print(solution(dices))