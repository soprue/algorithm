# https://www.acmicpc.net/problem/24313

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if a1 * n0 + a0 <= c * n0 and a1 <= c:
    print(1)
else:
    print(0)


# a0가 음수인 경우를 생각해 보면,
# 4*1 - 2 <= 2*1 (a1 = 4, a0 = -2, c = 2, n = 1)인 경우 성립하지만,
# 4*2 - 2 <= 2*2 (a1 = 4, a0 = -2, c = 2, n = 2)인 경우 성립하지 않는다.
# 따라서 a1 <= c 또한 확인해 주어야 해결할 수 있다 (이유는 c가 a1보다 크거나 같으면 음수가 있든 말든 보장 해주기 때문).
# https://clap0107.tistory.com/25
