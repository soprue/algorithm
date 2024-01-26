function solution(keymap, targets) {
    const answer = [];
    const map = {}
    for (const key of keymap) {
        key.split('').map((item, index) => map[item] = (map[item] < index+1 ? map[item] : index+1));
    }
    for (const target of targets) {
        answer.push(target.split('').reduce((cur, item) => cur += map[item], 0) || -1);
    }
    return answer;
}
