function solution(n, arr1, arr2) {
    return arr1.map((v, i) => {
        // |(비트 OR 연산) : 대응되는 비트 중에서 하나라도 1이면 1을 반환함
        return (v | arr2[i]).toString(2)
                            .padStart(n, 0)
                            .replace(/0/g,' ').replace(/1/g,'#')
    });
}
