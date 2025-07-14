/**
 * @param {number} n
 * @return {number}
 */
var trailingZeroes = function(n) {
    let count = 0;

    // 10이 만들어질 때마다 0이 하나 생김 (10 = 2 × 5)
    // 팩토리얼에는 2가 아주 많기 때문에(짝수마다 나와서), '5'가 몇 번 곱해졌는지를 세면 된다.
    while (n >= 5) {
        n = Math.floor(n / 5);
        count += n;
    }

    return count;
};
