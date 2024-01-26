function solution(cards1, cards2, goal) {
    var answer = [];
    
    goal.map(word => {
       if(word === cards1[0]) {
           answer.push(cards1.shift());
       } else if(word === cards2[0]) {
           answer.push(cards2.shift());
       } else {
           return "No";
       }
    });
    
    return JSON.stringify(answer) === JSON.stringify(goal) ? "Yes" : "No";
}
