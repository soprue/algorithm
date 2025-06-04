/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function(nums) {
    if (nums.length === 0) return [];

    const answer = [];
    let start = nums[0]; 

    for (let i = 1; i <= nums.length; i++) {
        // 연속이 아니면 지금까지의 구간을 저장
        if (i === nums.length || nums[i] !== nums[i - 1] + 1) {
            const end = nums[i - 1];
            if (start === end) {
                answer.push(`${start}`);
            } else {
                answer.push(`${start}->${end}`);
            }
            start = nums[i]; 
        }
    }

    return answer;
};
