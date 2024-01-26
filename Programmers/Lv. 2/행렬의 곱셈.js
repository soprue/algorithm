function solution(arr1, arr2) {
    const r1 = arr1.length; // arr1 행 개수
    const c1 = arr1[0].length; // arr1 열 개수 (== arr2 행 개수)
    const c2 = arr2[0].length; // arr2 열 개수
    
    // 결과 배열의 크기는 r1 * c2
    let answer = Array.from({length: r1}, () => new Array(c2));
    
    // arr1의 행마다 arr2의 열의 개수만큼 연산을 진행
    for (let i=0; i<r1; i++) {
        for (let j=0; j<c2; j++) {
            value = 0;
            for (let k=0; k<c1; k++) {
                // arr1의 i행에서 열의 인덱스 == arr2의 j열에서 행의 인덱스인 같은 원소끼리 곱하여 더해주기
                value += arr1[i][k] * arr2[k][j];    
            }
            answer[i][j] = value;
        }
    }
    
    return answer;
}
