/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    const count = new Map();

    for (const char of magazine) {
        count.set(char, (count.get(char) || 0) + 1);
    }

    for (const char of ransomNote) {
        if (!count.has(char) || count.get(char) === 0) {
            return false;
        }
        count.set(char, count.get(char) - 1);
    }

    return true;
};
