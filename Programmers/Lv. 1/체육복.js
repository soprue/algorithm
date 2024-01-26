function solution(n, lost, reserve) {
    let answer = 0;
    
    const students = {};
    for(let i = 1; i <= n; i++){
        students[i] = 1;
    }
    lost.forEach(number => students[number] -= 1);
    reserve.forEach(number => students[number] += 1);

    for(let i = 1; i <= n; i++){
        if(students[i] == 0 && students[i - 1] == 2) {
            students[i]++;
            students[i-1]--;
        } else if(students[i] == 0 && students[i + 1] == 2) {
            students[i]++;
            students[i+1]--;
        }
    }
    
    for(let key in students){
        if(students[key] > 0) answer++;
    }
    return answer;
}