import sys
input = sys.stdin.readline

N = int(input())
people = []
ranks = [1] * N

for _ in range(N):
    x, y = map(int, input().split())
    people.append((x, y))

for i in range(N):
    for j in range(N):
        if i != j:
            # i번 사람이 j번 사람보다 덩치가 작은 경우 i번 사람의 등수를 1증가
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                ranks[i] += 1

print(' '.join(map(str, ranks)))
