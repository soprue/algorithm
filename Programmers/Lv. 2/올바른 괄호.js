function solution(s){
    if(s[0] === ")") return false;
    
    let openCnt = 0;
    for(let i=0; i<s.length; i++) {
        if(s[i] === "(") openCnt += 1;
        else {
            openCnt -= 1;
            if (openCnt < 0) return false;
        }
    }
    
    return openCnt === 0;
}

// Stack에 '(' 하나의 문자만 누적된다면 자료구조를 사용하지 않고 int 변수에 개수만 +/- 시키는 것이 유리
