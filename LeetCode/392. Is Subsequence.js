/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    let i = 0; // s를 따라가는 포인터
    let j = 0; // t를 따라가는 포인터

    while (i < s.length && j < t.length) {
        if (s[i] === t[j]) {
            i++; // s의 다음 문자로 이동
        }
        j++; // t는 항상 다음 문자로 이동
    }
    
    return i === s.length;
};
