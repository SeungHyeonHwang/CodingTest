
def solution(n,names):
    return sorted(list(set(names)), key=lambda x : (len(x), x))

test_case = int(input())

for t in range(test_case) :
    n = int(input())
    names = []
    for _ in range(n):
        names.append(input())
    names = solution(n,names)
    print('#%d'%(t+1))
    for name in names:
        print(name)
