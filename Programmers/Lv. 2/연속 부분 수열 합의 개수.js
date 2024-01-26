function solution(elements) {
    let answer = new Set();
    const extendElements = [...elements, ...elements];
    
    for (let i = 0; i < elements.length; i++) {
        let sum = 0;
        for (let j = 0; j < elements.length; j++) {
            sum += extendElements[i + j];
            answer.add(sum);
        }
    }

    return answer.size;
}
