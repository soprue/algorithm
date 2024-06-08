function solution(x, y, n) {
    const calc = (a, op) => {
        switch(op) {
            case 0: return a - n;
            case 1: return (a % 2 === 0) ? a / 2 : 0;
            case 2: return (a % 3 === 0) ? a / 3 : 0;
        }
    }
    
    let queue = [[y, 0]];
    let visit = { [y]: true };
    
    while (queue.length) {
        let [cur, count] = queue.shift();
        if (cur === x) return count;

        for (let i = 0; i < 3; ++i) {
            let next = calc(cur, i);
            if (next >= x && !visit[next]) {
                visit[next] = true;
                queue.push([next, count + 1]);
            }
        }
    }

    return -1;
}

// [y부터 탐색 시작한 이유]
// y부터 시작해서 x로 가는 경로를 찾는 것은, x부터 시작해서 y로 가는 경로를 찾는 것보다 더 효율적일 수 있다. 특히, 연산을 할 때 나누기 연산이 곱하기 연산보다 더 제한적이기 때문에, 나누기 연산을 통해 가능한 모든 경로를 빠르게 찾을 수 있다.

// [BFS를 사용한 이유]
// BFS는 그래프나 트리에서 최단 경로를 찾는 데 사용된다. 이 문제에서는 x에서 y로 변환하는데 필요한 최소 연산 횟수를 찾는 것이 목표이므로, BFS가 적합하다.
