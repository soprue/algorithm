function solution(numbers, direction) {
    if(direction == "left") {
        let tmp = numbers.shift();
        numbers.push(tmp);
    } else {
        let tmp = numbers.pop();
        numbers.unshift(tmp);
    }
    return numbers;
}