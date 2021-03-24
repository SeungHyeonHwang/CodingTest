# 일곱 난쟁이

# 7 8 10 13 15 19 20 23 25
from itertools import combinations
dwarfs = [int(input()) for _ in range(9)]
lst = []
for com in combinations(dwarfs, 2):
	lst = [i for i in dwarfs if i not in com]
	if sum(lst) == 100:
		break
lst.sort()
for i in lst:
	print(i)
