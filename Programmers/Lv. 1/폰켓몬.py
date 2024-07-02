def solution(nums):
    myNum = len(nums) // 2
    setNums = len(set(nums))
    answer = myNum if setNums > myNum else setNums
    return answer
