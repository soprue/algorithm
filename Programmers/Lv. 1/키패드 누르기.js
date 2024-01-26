function solution(numbers, hand) {
    let leftHand = 10;
    let rightHand = 12;
    return numbers.map(num => {
        if(num == 0) num = 11;
        
        if(num % 3 == 1) return leftTo(num);
        else if(num % 3 == 0) return rightTo(num);
        else {
            const numLocation = numToLocation(num);
            const leftDistance = distanceBtwLocation( numToLocation(leftHand), numLocation );
            const rightDistance = distanceBtwLocation( numToLocation(rightHand), numLocation );
            
            if(leftDistance === rightDistance) return hand === "left" ? leftTo(num) : rightTo(num);
            else if(leftDistance < rightDistance) return leftTo(num);
            else if(leftDistance > rightDistance) return rightTo(num);
        }
    }).join("");

    function leftTo(num) {
        leftHand = num;
        return "L";
    }
    function rightTo(num) {
        rightHand = num;
        return "R";
    }
}

function numToLocation(num) {
    // 키패드를 4행 3열의 이차원 배열이라고 생각하고 좌표 구하기
    return [Math.floor((num - 1) / 3), (num - 1) % 3];
}

function distanceBtwLocation(a, b) {
    return Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]);
}