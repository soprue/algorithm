/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    if(!digits) return [];

    const result = [];

    const map = {
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z']
    };

    const backtrack = (index, path) => {
        if(index === digits.length) {
            result.push(path);
            return;
        }

        for(let letter of map[digits[index]]) {
            backtrack(index + 1, path + letter);
        }
    }

    backtrack(0, '');

    return result;
};
