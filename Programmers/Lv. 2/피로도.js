function solution(k, dungeons) {
    let answer = 0;
    
    // 방문했는지 확인하기 위한 배열
    const visited = Array.from({ length: dungeons.length }, () => false);
    
    // 완전탐색을 위한 DFS(남은 피로도, 진행단계)
    const DFS = (hp, L) => {
        for(let i=0; i<dungeons.length; i++) {
            if(!visited[i] && dungeons[i][0] <= hp) {
                visited[i] = true;
                DFS(hp - dungeons[i][1], L + 1);
                visited[i] = false;
            }
        }
        
        answer = Math.max(answer, L);
    }
    
    DFS(k, 0);
    
    return answer;
}

// https://leejams.github.io/%ED%94%BC%EB%A1%9C%EB%8F%84/
