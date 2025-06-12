/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    const mapST = {};  // s → t
    const mapTS = {};  // t → s

    for (let i = 0; i < s.length; i++) {
        const charS = s[i];
        const charT = t[i];

        // 이미 매핑된 경우 → 일치하는지 확인
        if (mapST[charS] && mapST[charS] !== charT) return false;
        if (mapTS[charT] && mapTS[charT] !== charS) return false;
        
        // 처음 보는 경우 → 매핑 등록
        mapST[charS] = charT;
        mapTS[charT] = charS;
    }

    return true;
};
