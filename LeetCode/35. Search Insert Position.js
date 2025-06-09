/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    let left = 0;
    let right = nums.length;

    while(left < right) {
        const mid = Math.floor((left + right) / 2);

        if(nums[mid] === target) {
            return mid; // 찾았으면 바로 리턴
        } else if(nums[mid] < target) {
            left = mid + 1; // 오른쪽으로 이동
        } else {
            right = mid; // 왼쪽으로 이동
        }
    }

    return left; // target이 없으면 들어갈 자리
};
