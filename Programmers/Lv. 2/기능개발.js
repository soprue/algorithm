function solution(progresses, speeds) {
    let answer = [];
    
    const developAccesses = progresses.map((progress, idx)=> Math.ceil((100 - progress) / speeds[idx]));
    let developedDay = developAccesses[0]
    let developedDayCount = 0;
    
    developAccesses.forEach(developAccess => {
        if(developedDay >= developAccess){
            developedDayCount++;
        } else {
            developedDay = developAccess;
            answer.push(developedDayCount);
            developedDayCount = 1;
        }
    })

    if(developedDayCount) {
        answer.push(developedDayCount);
    }
    
    return answer;
}
