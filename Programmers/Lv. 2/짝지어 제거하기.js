function solution(s)
{
    if(s.length % 2 === 1) return 0;
    
    let stack = [];
    for(let i = 0; i < s.length; i++) {   
        stack[stack.length - 1] == s[i] ? stack.pop() : stack.push(s[i]);
    };
    
    return stack[0] ? 0 : 1;
}
