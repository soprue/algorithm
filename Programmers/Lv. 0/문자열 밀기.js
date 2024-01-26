function solution(A, B) {
    if(A == B) return 0;
    
    let A_array = [...A];
    for(let i=1; i<=A_array.length; i++) {
        let last = A_array.pop();
        A_array.unshift(last);
        if(A_array.join("") == B) return i;
    }
    return -1;
}