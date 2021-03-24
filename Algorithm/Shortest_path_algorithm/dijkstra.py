# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 21:43:58 2021

@author: USER
"""

"""
7. 최단 경로 문제 
각 지점은 그래프에서 노드로 표현
지점 간 연결된 도로는 그래프에서 간선으로 표현 

1) 다익스트라 알고리즘 
특정한 노드에서 출발하여 다른 모든 노드로 가는 최단경로 계산
음의 간선이 없을 때 동작(다익스트라는 그리디 알고리즘으로 분류)
매 상황에서 가장 적은 노드를 선택해 과정을 반복 
 
*알고리즘 
 1. 출발노드 설정
 2. 최단 거리 테이블 초기화(자기 자신은 0, 나머지는 inf)
 3. 방문하지 않은 노드중에서 최단거리가 가장 짧은 노드 선택
 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 게산하여 최단거리 테이블 갱신
 5. 3~4 반복 
 
 *참고
 총 O(V)번에 걸쳐서 최단거리가 가장 짧은 노드를 매번 선형 탐색해야함
 따라서 전체 시간복잡도는 O(V^2)
 일반적으로 코딩테스트 최단 경로 문제에서는 전체 노드가 5,000개 이하라면 이코드로 문제해결 가능
 하지만 10,000이 넘어가면? 
 
 *우선순위 큐 (Priority Queue)
 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
 ex) 여러개 물건을 넣고 가치가 가장 높은 물건부터 꺼내야하는 경우

 *자료구조 (표준 라이브러리 존재)
 - stack : 가장 나중에 삽인된 데이터부터 나옴
 - queue : 가장 먼저 삽입된 데이터부터
 - priority queue : 가장 우선순위가 높은 데이터

 *heap을 통해 구현됨. 
 최소힙(min heap)과 최대힙(max heap)이 있음
 최소힙 : 값이 작은 데이터부터 꺼냄
 최대힙 : 값이 큰 데이터부터 꺼냄 
 
 *우선순위큐 구현 방식 
 1) 리스트를 이용하면 : 삽입시간 O(1), 삭제시간 O(N)
    삽입은 그냥 append로 넣음
    but, 삭제시 리스트 전체 조회 
 2) 힙을 이용하면 : 삽입시간 O(logN), 삭제시간 O(logN)
    heap은 내부적으로 트리구조를 이용 

 *다익스트라 개선된 구현 방법
 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 힙 자료구조 이용
 최단거리가 가장 짧은 노드를 선택하니까 최소힙 사용 
"""

# In[] : 다익스트라 알고리즘 

import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
        
        
# In[] : 우선순위 큐를 활용한 힙 정렬
"""
힙에 넣었다가 정렬상태로 빼기 O(NlogN)
python heapq는 기본적으로 min heap
"""

#import sys
import heapq
#input = sys.stdin.readline

# 오름차순
def minheapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = minheapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

# 내림차순
# -붙여서 넣었다가 그 값 찾아서 빼기 
def maxheapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = maxheapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

# In[] : 우선순위큐로 개선된 다익스트라 

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])