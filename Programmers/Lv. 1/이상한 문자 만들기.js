function solution(s) {
    return s.split(" ").map( (v) => [...v].map((x, idx) => {
        return idx % 2 == 0 ? x.toUpperCase() : x.toLowerCase();
    }).join("") ).join(" ");
}