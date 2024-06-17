function solution(begin, target, words) {
    if (!words.includes(target)) return 0;
    
    let queue = [[begin, 0]]; // 큐에 시작 단어와 변환 횟수를 함께 저장
    let visited = new Set([begin]); // 방문한 단어를 저장하는 집합
    
    while (queue.length > 0) {
        let [currentWord, steps] = queue.shift();
        
        if (currentWord == target) return steps;
        
        // 모든 단어에 대해 한 글자만 다른 단어 찾기
        for (let word of words) {
            if (!visited.has(word) && isTransformable(currentWord, word)) {
                visited.add(word);
                queue.push([word, steps + 1]);
            }
        }
    }
    
    return 0;
}

// 한 글자만 다른지 확인하는 함수
function isTransformable(word1, word2) {
    let diffCount = 0;
    
    for (let i=0; i<word1.length; i++) {
        if (word1[i] !== word2[i]) diffCount++;
        if (diffCount > 1) return false;
    }
    
    return diffCount === 1;
}
