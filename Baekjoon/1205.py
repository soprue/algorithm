import sys
input = sys.stdin.readline

N, new, P = map(int, input().split())
arr = list(map(int, input().split()))

arr.append(new)
arr.sort(reverse=True)
rank = arr.index(new) + 1

rank_index = arr.index(new) + 1
if arr.count(new) > 1:
    rank_index += arr.count(new) - 1

if rank_index > P:
    print(-1)
else:
    print(rank)
