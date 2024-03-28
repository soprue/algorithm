import sys

N = int(sys.stdin.readline().strip())

file = {}

for _ in range(N) :
    _, extension = sys.stdin.readline().strip().split(".")
    file[extension] = file.get(extension, 0) + 1

for extension in sorted(file):
    print(extension, file[extension])