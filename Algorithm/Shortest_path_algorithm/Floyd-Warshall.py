# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 15:13:24 2021

@author: USER
"""


"""
플로이드 워셜 알고리즘(Floyd-Warshall)

모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산
2차원 테이블에 최단 거리정보를 저장
다이나믹 프로그래밍 유형

*점화식
 a에서 b로 가는 최단거리보다 a에서 k를 거쳐 b로 가는 거리가 더 짧은지 검사 
 Dab = min(Dab, Dak + Dkb)


*성능
노드가 N개일때, 각 단계마다 O(N^2) 연산을 통해 현재 노드를 거쳐 가는 모든 경로를 고려
따라서 시간 복잡도는 O(N^3)

"""

# In[] : Floyd-Warshall

INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        if graph[a][b] == 1e9:
            print("INFINITY", end=" ")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(graph[a][b], end=" ")
    print()