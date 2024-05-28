function solution(word) {
    const vowels = ["A", "E", "I", "O", "U"];
    let count = 0;
    let result = 0;
    
    function dfs(current) {
        if(current === word) {
            result = count;
            return;
        }
        if (current.length === 5) {
            return;
        }
        
        for (let i = 0; i < vowels.length; i++) {
            count++;
            dfs(current + vowels[i]);
        }
    }
    
    dfs("");
    return result;
}
