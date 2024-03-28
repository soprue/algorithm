import sys

N = int(sys.stdin.readline().strip())

company = {}

for _ in range(N) :
    name, status = sys.stdin.readline().strip().split()
    if status == "enter" :
        company[name] = True
    else:
        del company[name]

print("\n".join(sorted(company.keys(), reverse=True)))