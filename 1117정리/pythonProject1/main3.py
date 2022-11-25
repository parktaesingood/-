import heapq

N = int(input())
M = int(input())
arr = [[] for _ in range(N)]
for i in range(M):
    a,b,c = map(int,input().split())

    arr[a].append((b,c))

heap = []
result = [float('inf')] * N
start,end = map(int,input().split())
def dijkstra(start):
    heapq.heappush(heap,(0,start))
    result[start] = 0

    while heap:
        sk, k = heapq.heappop(heap)

        if result[sk] < k:
            continue

        for i in arr[k]:
            cost = sk + result[i[1]]
            if result[i[0]] < cost:
                cost = result[i[0]]
                heapq.heappush(heap,(cost,i[0]))

dijkstra()
