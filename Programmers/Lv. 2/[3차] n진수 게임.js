function solution(n, t, m, p) {
    // 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p
    let orderNumber = new Array(t).fill().map((_, index) => index * m + p - 1);
    
    var str = "";
    var max = m * t + p;
    for (let i = 0; str.length <= max; i++) {
        str += i.toString(n);
    }
    
    return orderNumber.map(element => str[element]).join("").toUpperCase();
}
