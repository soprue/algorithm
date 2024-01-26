function solution(a, b, n) {
    let fullBottle = 0;
    let emptyBottle = n;

    while(emptyBottle >= a) {
        let get = Math.floor(emptyBottle / a) * b;
        fullBottle += get;
        emptyBottle = get + (emptyBottle % a);
    }
    
    return fullBottle;
}