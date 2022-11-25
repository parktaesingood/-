TC = int(input())

for tc in range(1,TC+1):

    N = int(input())
    arr = list(map(int,input().split()))
    cnt,flag = 0,True
    ed = max(arr)

    if min(arr) == ed:
        pass
    else:
        while flag:
            cnt += 1
            if cnt % 2 == 1:
                for i in range(N):
                    if arr[i] + 2 == ed:
                        continue
                    elif i-1 == N and arr[i] + 2 == ed:
                        break
                    elif arr[i] < ed:
                        arr[i] += 1
                        break
            else:
                for i in range(N):
                    if arr[i] + 2 <= ed:
                        arr[i] += 2
                        break
            if min(arr) == ed:
                flag = False

    print(f'#{tc} {cnt}')