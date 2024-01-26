function solution(survey, choices) {
    let answer = '';
    let type = {
        R: 0,
        T: 0,
        C: 0,
        F: 0,
        J: 0,
        M: 0,
        A: 0,
        N: 0,
    };
    let score = [3, 2, 1, 0, 1, 2, 3];
    
    choices.forEach((choice, index) => {
        const [disagree, agree] = survey[index];
        type[choice > 4 ? agree : disagree] += Math.abs(choice - 4);
    });
    
    answer += type["T"] > type["R"] ? "T" : "R";
    answer += type["F"] > type["C"] ? "F" : "C";
    answer += type["M"] > type["J"] ? "M" : "J";
    answer += type["N"] > type["A"] ? "N" : "A";
    return answer;
}