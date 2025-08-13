import sys

input = sys.stdin.readline

N, K, Q, M = map(int, input().strip().split())

sleep = [False] * (N + 3) # 0~N+2
for x in map(int, input().split()):
    sleep[x] = True

senders = list(map(int, input().split()))  # Q명

attend = [0] * (N + 3)

for sender in senders:
  if sleep[sender]:
    continue
  for i in range(sender, N + 3, sender):
    if not sleep[i]:
      attend[i] = 1

# "결석자 수"에 대한 누적합
prefix_absent = [0] * (N + 3)
for i in range(3, N + 3):
  absent = 1 - attend[i]
  prefix_absent[i] = prefix_absent[i - 1] + absent

for _ in range(M):
  S, E = map(int, input().strip().split())
  print(prefix_absent[E] - prefix_absent[S - 1])20438
