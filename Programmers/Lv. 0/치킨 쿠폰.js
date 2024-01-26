function solution(chicken) {
    let service = 0;
    let coupon = chicken;
    
    while(coupon >= 10) {
        let bonus = Math.floor(coupon / 10);
        service += bonus;
        coupon = coupon % 10 + bonus;
    }
    return service;
}