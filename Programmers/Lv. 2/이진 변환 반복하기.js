function solution(s) {
    let count = 0;
    let removal = 0;
    
    do {
        count++;
        removal += (s.match(/0/g) || []).length;
        s = s.replace(/0/g, '').length.toString(2);
    } while(s !== "1");
    
    return [count, removal];
}
