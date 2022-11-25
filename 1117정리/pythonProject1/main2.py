# import copy
#
# TC = int(input())
# for tc in range(1,TC+1):
#     now, pay = map(int, input().split())
#     N, M = map(int, input().split())
#     n = copy.deepcopy(now)
#     future = 0
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     for i in range(N):
#         arr[i].append(0)
#
#     def dfs(i,level):
#         global tmp,future,now,mmax,money
#
#         if tmp > now:
#             return
#
#         if mmax < future:
#             mmax = future
#             money = copy.deepcopy(future)
#
#         for k in range(N):
#             tmp += arr[k][i]
#             future += (arr[k][i+1] - arr[k][i])
#             dfs(i,level+1)
#             tmp -= arr[k][i]
#             future -= (arr[k][i+1] - arr[k][i])
#
#
#     for i in range(M):
#         tmp = 0
#         mmax = 0
#         money = 0
#         dfs(i,0)
#         now = now + money + pay
#
#     m = pay*M
#
#     print(f'#{tc} {now-m-n}')

# import copy
#
# TC = int(input())
# for tc in range(1,TC+1):
#     now, pay = map(int, input().split())
#     N, M = map(int, input().split())
#     n = copy.deepcopy(now)
#     path = [''] * 10
#     future = 0
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     for i in range(N):
#         arr[i].append(0)
#
#     def dfs(i,level):
#         global tmp,future,now,mmax,money
#
#         if tmp > now:
#             return
#
#         print(path)
#         if mmax < future:
#             mmax = future
#             money = copy.deepcopy(future)
#
#         for k in range(N):
#             path[level] = arr[k][i]
#             tmp += arr[k][i]
#             future += (arr[k][i+1] - arr[k][i])
#             dfs(i,level+1)
#             path[level] = ''
#             tmp -= arr[k][i]
#             future -= (arr[k][i+1] - arr[k][i])
#
#
#     for i in range(M):
#         tmp = 0
#         mmax = 0
#         money = 0
#         dfs(i,0)
#         now = now + money + pay
#
#     m = pay*M
#
#     print(f'#{tc} {now-m-n}')


# N = 3
# path = ['']*3
# arr = [1,2,3]
#
# def dfs(level,st):
#     if level == N:
#         for i in range(len(path)):
#             print(path[i],end= ' ')
#         print()
#         return
#
#     for k in range(st,N):
#         path[level] = arr[k]
#         st = k
#         dfs(level+1,st)
#
# dfs(0,0)

import copy

TC = int(input())
for tc in range(1,TC+1):
    now, pay = map(int, input().split())
    N, M = map(int, input().split())
    n = copy.deepcopy(now)
    future = 0
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        arr[i].append(0)

    def dfs(i,level,st):
        global tmp,future,now,mmax,money

        if tmp > now:
            return

        if mmax < future:
            mmax = future
            money = copy.deepcopy(future)

        for k in range(st,N):
            tmp += arr[k][i]
            future += (arr[k][i+1] - arr[k][i])
            st = k
            dfs(i,level+1,st)
            tmp -= arr[k][i]
            future -= (arr[k][i+1] - arr[k][i])


    for i in range(M):
        print(i)
        tmp = 0
        mmax = 0
        money = 0
        dfs(i,0,0)
        now = now + money + pay

    m = pay*M

    print(f'#{tc} {now-m-n}')

