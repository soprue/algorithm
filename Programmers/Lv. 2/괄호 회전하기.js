function solution(s) {
    if(s.length % 2 === 1) return 0;
    
    let answer = 0;
    const mapping = { "}" : "{", "]" : "[", ")" : "("};
    
    for(let i=0; i<s.length; i++) {
        const newString = s.substr(i) + s.substr(0, i);
        let stack = [];
        let flag = true;
        
        for(let char of newString) {
            if(char == "(" || char == "[" || char == "{") {
                stack.push(char);
            } else {
                if(stack.pop() !== mapping[char]) {
                    flag = false;
                    break;
                }
            }
        };
        
        if(flag) answer++;
    }
    
    return answer;
}
