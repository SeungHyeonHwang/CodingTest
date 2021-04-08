



from collections import Counter

n,m = map(int, input().split())
maps = [list(map(str, input())) for _ in range(n)]

answer = 0
ans_dna = ''
names = 'TAGC'
for i in range(m):
	DNA = {string:0 for i,string in enumerate(names)}
	for j in range(n):
		DNA[maps[j][i]]+=1

	max_dna = sorted(DNA.items(), key=lambda x:(-x[1],x[0]))[0]
	answer+=n-max_dna[1]
	ans_dna+=max_dna[0]

print(ans_dna)
print(answer)
