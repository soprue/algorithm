function solution(k, score) {
    var stack = [];
    
    return score.map((v) => {
        if(stack.length < k) stack.push(v);
        else {
            if(v >= stack[k - 1]) stack[k - 1] = v;
        }
        
        stack.sort((a, b) => b - a);
        return stack[stack.length - 1];
    })
}