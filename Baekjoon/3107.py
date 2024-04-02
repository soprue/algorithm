# https://www.acmicpc.net/problem/3107

ip = input().split(":")

if '' in ip:
    index = ip.index('')
    ip.remove('')
    while len(ip) < 8:
        ip.insert(index, '0000')

for i in range(8):
    ip[i] = ip[i].zfill(4)

print(":".join(ip))
