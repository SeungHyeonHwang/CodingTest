
def twoSum(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: List[int]
	"""

	ans = []
	dictionary = {}
	for i,num in enumerate(nums) :	
		if num not in dictionary.keys() :
			dictionary[num] = [i]
		else : 
			dictionary[num].append(i)
	for i,num in enumerate(nums) :	
		if target-num in dictionary.keys() :
			if dictionary[target-num] == [i] :
				continue
			if target-num == num : 
				ans.append(dictionary.get(target-num)[0])
				ans.append(dictionary.get(num)[1])
				break
			else :
				ans.append(dictionary[target-num][0])
				ans.append(dictionary.get(num)[0])
				break
	return sorted(ans)
print(twoSum([2,5,5,11],10))