function solution(n, computers) {
    let answer = 0;
    let visited = [];
    
    function dfs(node, visited, computers) {
        visited[node] = true;
        for(let i=0; i<computers.length; i++) {
            // 연결된 노드가 있고 해당 노드를 방문하지 않았다면 dfs로 방문 진행
            if(computers[node][i] === 1 && !visited[i]) dfs(i, visited, computers); 	
        }
    }
    
    for (let i=0; i<computers.length; i++) {
        if (!visited[i]) {
            dfs(i, visited, computers);
            answer++;
        }
    }
    
    return answer;
}

