function solution(my_string) {
    return [...my_string]
        .map(v => {
            if(v == v.toUpperCase()) return v.toLowerCase();
            else return v.toUpperCase();
        })
        .join("");
}