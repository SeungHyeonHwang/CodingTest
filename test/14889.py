


def get_power(team):
	teamPower = 0
	for i in team:
		for j in team:
			if i!=j :
				teamPower+=power[i][j]
	return teamPower

def solution(n):
	answer = int(1e9)
	total = [i for i in range(n)]
	for team1 in combinations(total, n//2):
		team2 = list(set(total)-set(team1))
		answer= min(answer, abs(get_power(team1)-get_power(team2)))
	return answer

from itertools import combinations
n = int(input())
power = [list(map(int, input().split())) for _ in range(n)]
print(solution(n))
