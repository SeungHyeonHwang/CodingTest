
def handPos(n, hand) : 
	for i in range(4) :
		for j in range(3) : 
			if phone[i][j] == n :
				hand = [i,j]
	return hand

def calDist(n, hand, left_hand_pos, right_hand_pos) : 
	for i in range(4) :
		for j in range(3) : 
			if phone[i][j] == n :
				x,y=i,j
				break
	left_dist = abs(left_hand_pos[0] - x) + abs(left_hand_pos[1] - y)
	right_dist = abs(right_hand_pos[0] - x) + abs(right_hand_pos[1] - y)
	
	print('n:',n, 
	phone[left_hand_pos[0]][left_hand_pos[1]], 
	phone[right_hand_pos[0]][right_hand_pos[1]])
	print('l :',left_dist, 'r :', right_dist)
	print()
	if left_dist > right_dist :
		right_hand_pos =[x,y]
		return ["R", right_hand_pos] 
	elif left_dist < right_dist : 
		left_hand_pos =[x,y]
		return ["L", left_hand_pos] 
	else : # 거리 같으면
		if hand == "right" : 

			right_hand_pos =[x,y]
			return ["R", right_hand_pos] 
		else :
			left_hand_pos =[x,y]
			return ["L", left_hand_pos] 


def solution(numbers, hand):
	answer = ''
	left_hand_pos = [3,0]
	right_hand_pos = [3,2]

	for n in numbers : 
		if n == 1 or n == 4 or n == 7 :
			answer+="L"
			left_hand_pos = handPos(n, left_hand_pos)
		elif n == 3 or n == 6 or n == 9 :
			answer+="R"
			right_hand_pos = handPos(n, right_hand_pos)
		else : 
			result = calDist(n, hand, left_hand_pos, right_hand_pos)
			answer+=result[0]
			if result[0] == "L" : left_hand_pos = result[1]
			else : right_hand_pos = result[1]
	return answer


phone = [[1,2,3],[4,5,6],[7,8,9],[10,0,11]]
numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	
hand = "right"

print(solution(numbers, hand))