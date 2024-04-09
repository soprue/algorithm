# https://www.acmicpc.net/problem/2839

N = int(input())

# 5킬로그램 봉지 최대 사용 가능 개수
bag5 = N // 5

while bag5 >= 0:
    # 남은 무게 계산
    remaining = N - bag5 * 5
    
    # 남은 무게가 3의 배수인 경우
    if remaining % 3 == 0:
        # 3킬로그램 봉지 개수 계산
        bag3 = remaining // 3
        # 총 봉지 개수 출력
        print(bag5 + bag3)
        break
    else:
        # 5킬로그램 봉지 사용 개수를 하나 줄임
        bag5 -= 1
else:
    # 정확하게 N킬로그램을 만들 수 없는 경우
    print(-1)
