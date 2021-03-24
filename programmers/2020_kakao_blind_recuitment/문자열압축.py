

def solution(s):
	answer = 0
	cand_ans = []
	cand_ans.append(len(s))
	# 1부터 (len(s)//2) +1 까지 반복 문자열 
	for n in range(1, (len(s)//2)+1) : 
		chunk = []
		chunk.append([1, s[:n]])
		cnt = 0
		# n 부터 s 끝까지 조사, n 는 반복 길이
		for i in range(n,len(s),n) :
			if s[i: i+n] == chunk[cnt][1] :
				chunk[cnt][0] +=1

			else :
				chunk.append([1, s[i: i+n]])
				cnt +=1	
		# chunk들을 정답 포맷으로 바꿔줌
		temp = ''
		for num, c in chunk :
			if num == 1 :
				temp += c
			else :
				temp += str(num) + c
				i+=1
		
		if len(temp) != 0 : 
			cand_ans.append(len(temp))
	answer = sorted(cand_ans)[0]
	return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
