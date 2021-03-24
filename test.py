


def solution(skill, skill_trees):
	answer = 0
	def check_possible(user_skill):
		j=0
		for i in range(len(user_skill)):
			if user_skill[i]==skill[j]:
				j+=1
				if j==len(skill):
					break
				for s in skill[j:]:
					if s in user_skill[:i]:
						return 0
		if i==0:
			return 0
		print(user_skill)
		return 1

	for user_skill in skill_trees:
		answer+=check_possible(user_skill)
	print(answer)
	return answer

solution("ABC",["CB", "CA", "AC", "A"])