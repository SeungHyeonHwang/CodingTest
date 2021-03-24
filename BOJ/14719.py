
"""
빗물 
- 시뮬/brute-force
- 참고 : https://incastle-study.tistory.com/2
- 해결 아이디어 : 양 옆보다 내가 작으면 정답에 저장
"""
def solution(h,w):
	answer = 0 

	max_left, max_right = 0,0
	for i in range(w):
		
		max_left = max(block[:i+1])
		max_right = max(block[i:])
		which_low = min(max_left, max_right)
		answer += which_low - block[i]

	return answer


h,w = map(int, input().split())
block = list(map(int, input().split()))
print(solution(h,w))