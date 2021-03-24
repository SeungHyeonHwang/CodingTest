# In[] : # 정렬
"""

1. 선택정렬
처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨앞에 있는 데이터와 바꾸는 것을 반복   
연산 횟수
N + (N-1) + (N-2) + ... + 2
= (N^2 + N - 2)/2 이고 빅오표기법에 따라 O(N^2)

"""
# 코드
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소 인덱스
    for j in range(i+1, len(array)) :
        if array[min_index] > array[j] : 
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)

"""
2. 삽입정렬
처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
구현 난이도 높지만 일반적으로 더 효율적 
시간복잡도 O(N^2)이며, 현재 데이터가 거의 정렬되어 있는 상태라면 매우 빠름
최선의 경우 O(N)
"""
# 코드
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i 부터 1까지 1씩 감소하며 반복 
        if array[j] < array[j-1] : # 한칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else : # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
print(array)


"""
3. 퀵정렬
기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터 위치를 바꾸는 방법
일반적인 상황에서 가장 많이 사용
가장 기본적인 퀵정렬은 첫번째 데이터를 기준 데이터(Pivot)로 설정 
시간복잡도 평균 O(NlogN), 최악(최대,최소가 pivot일 때 ) O(N^2) (분할이 안되고 한쪽으로 쏠릴 경우)
https://zeddios.tistory.com/35
"""
# 코드

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복 
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)


# 컴프리헨션 이용 버전 
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort_comp(array) : 
    if len(array) <= 1 : 
        return array
    pivot = array[0]
    tail = array[1:]
    left_side = [x for x in tail if x <= pivot] # tail에서 피벗보다 작으면 담음
    right_side = [x for x in tail if x > pivot] # tail에서 피벗보다 크면 담음
    
    return quick_sort_comp(left_side) + [pivot] + quick_sort_comp(right_side)
print(quick_sort_comp(array))

"""
4. 계수 정렬
특정 조건 부합시 사용 가능. 매우빠름
데이터 크기 범위가 제한되어 정수 형태로 표현 할 수 있을 때 사용가능
데이터 개수가 N 데이터 양수 최대값 K일때 최악의 경우 수행시간 O(N+K)
계수정렬 시간 및 공간 복잡도는 모두 O(N+K)
때에 따라 심각한 비효율성을 보여줌
예) 데이터가 0과 999,999로 단 2개만 존재하는 경우, 리스트가 매우 커짐 1 0 0 ... 0 0 1
계수 정렬은 동일한 값을 가지는 데이터가 여러 개 등장할 때 효과적 
"""
# 코드 
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력

