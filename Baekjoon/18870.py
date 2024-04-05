# https://www.acmicpc.net/problem/18870

N = int(input())
X = list(map(int, input().split()))

# 좌표를 키로, 압축 결과를 값으로 하는 딕셔너리 생성
dict = {x: i for i, x in enumerate(sorted(set(X)))}

# 각 좌표에 대해 압축 결과를 리스트에 저장
compressed = [str(dict[x]) for x in X]

# 리스트를 공백으로 구분된 문자열로 변환하여 한 번에 출력
print(" ".join(compressed))
