function solution(n, words) {
    let stack = [];

    for(let i=0; i<words.length; i++) {
        // 중복 단어 말한 경우
        if(stack.includes(words[i])) {
            let number = (i + 1) % n === 0 ? n : (i + 1) % n;
            let count = Math.ceil((i + 1) / n);
            return [number, count];
        } else {
            let last = stack[stack.length - 1];
            // 끝말잇기 틀린 경우
            if(i !== 0 && last[last.length - 1] !== words[i][0]) {
                let number = (i + 1) % n === 0 ? n : (i + 1) % n;
                let count = Math.ceil((i + 1) / n);
                return [number, count];
            }
            stack.push(words[i]);
        }
    }
    
    return [0, 0];
}
