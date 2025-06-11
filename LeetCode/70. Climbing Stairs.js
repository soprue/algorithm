/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    if(n <= 2) return n;

    let oneStepBefore = 2; // f(n - 1)
    let twoStepBefore = 1; // f(n - 2)

    for(let i=3; i<=n; i++) {
        result = oneStepBefore + twoStepBefore;
        twoStepBefore = oneStepBefore;
        oneStepBefore = result;
    }

    return result;
};
