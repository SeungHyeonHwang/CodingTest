
def solution(skill, skill_trees):
	answer = len(skill_trees)
	skillOrder = {string:i for i,string in enumerate(skill)}

	for tree in skill_trees :
		check = 0 
		for each_skill in tree : 
			if each_skill in skillOrder and check == skillOrder[each_skill] : 
				check+=1
			elif each_skill in skillOrder and check != skillOrder[each_skill] : 
				answer-=1
				break
	return answer 

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))

