# https://www.acmicpc.net/problem/11478

S = input()

length = len(S)
string = set()

for i in range(length):
    for j in range(i, length):
        string.add(S[i : j+1])

print(len(string))
