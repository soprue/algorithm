const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

// 모듈로 상수는 BigInt로 선언하여 큰 수 연산에서 발생할 수 있는 오버플로를 방지합니다.
const MODULO = BigInt(1000000007);

rl.on("line", (input) => {
    // JavaScript의 일반 Number 타입은 약 9x10^15 이상의 큰 정수를 정확하게 처리할 수 없으므로
    // 바이러스 개수의 증가 계산을 정확하게 처리하기 위해 BigInt를 사용합니다.
    const [K, P, N] = input.split(" ").map(BigInt);
    
    let virusCount = K;
    for(let i=0; i<N; i++) {
        virusCount = (virusCount * P) % MODULO;
    }

    // BigInt 결과를 문자열로 변환하여 출력합니다.
    console.log(virusCount.toString());

    rl.close();
});
