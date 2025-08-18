import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

# nCm 값을 저장해 둘 표
dp = [[-1] * 101 for _ in range(101)]

def comb(n, m):
  if m == 0 or m == n:
    return 1
  if dp[n][m] != -1:
    return dp[n][m]

  dp[n][m] = comb(n - 1, m - 1) + comb(n - 1, m)
  
  return dp[n][m]

n, m = map(int, input().strip().split())
print(comb(n, m))
