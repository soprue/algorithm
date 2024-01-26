function solution(phone_book) {
    const hashMap = {};

    for (const number of phone_book) {
        hashMap[number] = true;
    };

    for (const number of phone_book) {
        for (let i = 1; i < number.length; i++) {
            const prefix = number.slice(0, i);
            if (hashMap[prefix]) return false;  
        };
    };

    return true;
}

// 일반적인 경우에서, 객체의 프로퍼티 접근은 매우 최적화되어 있기 때문에 Map보다 더 빠를 수 있다.
// 이 문제의 경우, 전화번호를 문자열로 처리하고 있으므로 객체의 키로 사용하는 것에 문제가 없다.
// 따라서 객체를 사용하여 프로퍼티에 접근하는 것이 Map의 메서드를 사용하는 것보다 더 빠를 수 있다.
// 만약 키의 순서가 중요하거나, 키로 객체나 함수 등의 복잡한 데이터 타입을 사용해야 하는 경우 Map을 사용하는 것이 좋다.
