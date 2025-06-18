/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function(n) {
    let binary = n.toString(2).toString();
    return binary.match(/1/g).length;
};
