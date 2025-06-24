/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    const seen = new Set(); // 지금까지 나온 숫자 저장 (무한루프 방지)

    while (n !== 1 && !seen.has(n)) {
        seen.add(n);         
        n = getNext(n);       
    }

    return n === 1; 

    function getNext(num) {
        let sum = 0;
        while (num > 0) {
            let digit = num % 10;       
            sum += digit * digit;      
            num = Math.floor(num / 10); 
        }
        return sum;
    }
};
