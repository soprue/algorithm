function solution(skill, skill_trees) {
    let answer = 0;
    
    skill_trees.forEach((tree) => {
        let skillIndex = 0;
        let flag = true;

        for (const char of tree) {
            const index = skill.indexOf(char);
            if (index >= 0) { // 현재 스킬이 선행 스킬 순서에 포함되는 경우
                if (index === skillIndex) {
                    skillIndex++; // 선행 스킬 순서에 맞게 다음 스킬을 기대
                } else {
                    flag = false;
                    break; // 순서가 맞지 않으므로 더 이상 검사할 필요 없음
                }
            }
        }

        if (flag) answer++;
    });
    
    return answer;
}
