function solution(s, skip, index) {
    var answer = '';
    let skipArr = [];
    
    for (let i = 0; i < skip.length; i++) {
        skipArr.push(skip.charCodeAt(i));
    }
    
    s.split("").forEach(ele => {
        let code = ele.charCodeAt();
        for(let i = 0; i < index; i++) {
            do {
                code++;  
                if (code > 122) code = 97;
            } while (skipArr.includes(code));
        }
        answer += String.fromCharCode(code);
    })
    
    return answer;
}
