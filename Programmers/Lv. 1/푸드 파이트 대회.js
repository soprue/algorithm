function solution(food) {
    var answer = [0];
    for(let i = food.length - 1; i >= 1; i--) {
        let half = Math.floor(food[i] / 2);
        answer.push(i.toString().repeat(half));
        answer.unshift(i.toString().repeat(half));
    }
    return answer.join("");
}