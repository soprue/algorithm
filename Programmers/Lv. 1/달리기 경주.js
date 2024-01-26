function solution(players, callings) {
    const idxs = {};
    for (let i = 0; i < players.length; i++) {
        idxs[players[i]] = i;
    }

    callings.forEach((player) => {
        const curIdx = idxs[player];
        [players[curIdx - 1], players[curIdx]] = [players[curIdx], players[curIdx - 1]];

        idxs[player]--;
        idxs[players[curIdx]]++;
    });
    
    return players;
}

// players의 최대 길이는 50,000이고, callings의 최대 길이는 1,000,000이므로 forEach와 indexOf를 사용하여 문제를 풀이하면 시간 초과 이슈 발생
// -> Map을 활용하여 문제 풀이

// indexOf는 배열을 순차적으로 검색하면서 값을 찾으므로 선형 검색(linear search) 알고리즘을 사용
// 최악의 경우, indexOf는 배열의 모든 요소를 확인해야 함 -> 따라서 배열의 크기에 따라 성능이 선형적으로 증가함

// Map은 키-값 쌍을 저장하는 자료구조
// Map을 사용하면 특정 키에 대한 값을 상수 시간(상수 시간 복잡도)으로 검색할 수 있음 -> 검색 시간은 키의 개수에 관계없이 일정함
