
# 문자열

string = "ABCdefC"
print(string.lower()) # 소문자
print(string.upper()) # 대문자 
print(string[0].isupper()) # 대문자인가
print(string.replace("A", "G")) # 대체

index = string.index("C") # 인덱스 
print(index)
print(string.index("C", index+1)) # 그 다음 위치 
print(string.find("C"))
print(string.find("AAA")) # 없으면 -1, index로 찾으면 ValueError 발생
print(string.count("C")) # 몇갠지 


# 사전 자료형

cabinet = {0:"유재석", 3:"김태호"}
#print(cabinet[2]) # 에러
print(cabinet.get(2)) # None
print(cabinet.get(0, "사용가능")) # 유재석
print(cabinet.get(2, "사용가능")) # 사용가능 
print(cabinet)

cabinet[1] = "조세호" # 새 키-값 입력
print(cabinet)
del cabinet[1]
print(cabinet)


# 집합 set

java = {"유재석", "김태호", "양세형"}
python = {"유재석", "박명수"}
print(java & python) # 교 
print(java.intersection(python)) # 교 

print(java | python) # 합
print(java.union(python))

print(java - python) # 차 
print(java.difference(python))

python.add("김태호") # 원소 추가 
print(python)

python.remove("김태호")
print(python)


# lambda 함수
"""
 - 익명함수 : 메모리를 아끼고 가독성을 향상시킨다. pythonic
 - 일반적인 함수는 객체를 만들고, 재사용을 위해 함수 이름(메모리)를 할당한다.

* lambda는 왜 쓰는가?
 - 익명함수이기 때문에 한번 쓰이고 다음줄로 넘어가면 힙(heap) 메모리 영역에서 증발
 - (참고) 가비지 컬렉터 (참조하는 객체가 없으면 지워버린다)
 - 파이썬에서는 모든것이 객체로 관리 되고 각 객체들은 레퍼런스 카운터를 갖게 된다. 이 카운터가 0 즉, 그 누구도 참조하지 않게 된다면 메모리를 환원 하게 된다.
"""
sum = lambda a, b: a+b
sum(3,4)


# map 함수
"""
 - map으로 짜면 게으른 연산을 진행해서 메모리를 크게 절약할 수 있다.
 - map의 연산 결과는 map iterator 객체로 리턴한다.
"""
# Input : li = [1, 2, 3]
# Output : result = [1, 4, 9]

# 풀이
li = [1, 2, 3]
result = list(map(lambda i: i ** 2 , li))


# 게으른 연산
"""
(참고) 게으른 연산
 - 필요할 때 가져다 쓴다.(예: map함수의 결과 객체)
 - iterator 객체
 - next() 메소드로 데이터를 순차적으로 호출 가능한 object
 - 마지막 데이터까지 불러 오면 다음은 StopIteration exception 발생
 -iterable한 객체를 iterator 로 변환하고 싶다면, iter() 라는 built-in function 을 사용
 - for 문으로 looping 하는 동안, python 내부에서는 임시로 list를 iterator로 자동 변환
"""
# ex1.
li = [1, 2, 3]
result = map(lambda i: i * i, li)
next(result) # 1
next(result) # 4
next(result) # 9
#next(result) # StopIteration 발생


# filter 함수

"""
filter(함수, literable)
두번째 인수인 반복 가능한 자료형 요소들을 첫번째 인자 함수에 하나씩 입력하여 리턴값이 참인 것만 묶어서 돌려준다.
함수의 리턴 값은 참이나 거짓이어야 한다.
"""
li = [-2, -3, 5, 6]

# 양수만 반환하는 리스트
def ft(li):
    result = []
    for e in li:
        if e > 0:
            result.append(e)
        else:
            pass
    return result

# filter 함수 사용시
def positive(x):
  return x > 0

list(filter(positive, li))

# filter + lambda 함수 사용시
list(filter(lambda x: x > 0, li))


# reduce 함수 

from functools import reduce
reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
# = ((((1+2)+3)+4)+5)

# 문제1. reduce 활용하여 최대값 구하기
reduce(lambda a,b: a if a > b else b ,li)

from collections import Counter
data = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c']
print(dict(Counter(data)))