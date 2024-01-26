// https://school.programmers.co.kr/learn/courses/30/lessons/12977

// 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.
// 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때,
// nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.



function isPrime(num) {
    for(let i=2; i<=Math.sqrt(num); i++) {  
        if (num % i === 0) return false;  
    }  
    return true;
}

function solution(nums) {
    let answer = 0;
    
    const combination = (current, start) => {
        if(current.length == 3) {
            let sum = current.reduce((acc, cur) => acc + cur, 0);
            if(isPrime(sum)) answer++;
            return;
        }
        
        for(let i=start; i<nums.length; i++) {
            combination([...current, nums[i]], i + 1);
        }
    }
    
    combination([], 0);
    
    return answer;
}
