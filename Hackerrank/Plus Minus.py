def plusMinus(arr):
    total = len(arr)
    positive = sum(1 for num in arr if num > 0)
    negative = sum(1 for num in arr if num < 0)
    zero = sum(1 for num in arr if num == 0)
    
    print(f"{positive / total:.6f}")
    print(f"{negative / total:.6f}")
    print(f"{zero / total:.6f}")

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
