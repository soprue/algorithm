function solution(s) {
    let answer = [];

    let string = "";
    let x = 0, another = 0;

    for(let i=0; i<s.length; i++) {
        if(string === "") string += s[i];

        if(string[0] === s[i]) x++;
        else another++;
        string += s[i];

        if(x === another) {
            answer.push(string);
            string = "";
        }
        if(string !== "" && i === s.length - 1) {
            answer.push(string);
        }
    }

    return answer.length;
}