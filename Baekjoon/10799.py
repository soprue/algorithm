# https://www.acmicpc.net/problem/10799

string = input().strip()
stack = []
answer = 0

for i in range(len(string)):
    if string[i] == '(':
        stack.append('(')
    else:
        if string[i-1] == '(':  # 바로 직전이 여는 괄호라면 레이저
            stack.pop()
            answer += len(stack)  # 스택에 남아 있는 여는 괄호의 수만큼 조각 수 증가
        else:  # 쇠막대기의 끝
            stack.pop()  # 스택에서 짝꿍 여는 괄호 제거
            answer += 1  # 쇠막대기 끝 부분도 조각으로 카운트

print(answer)
