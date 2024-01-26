function solution(rsp) {
    return [...rsp].map(v => v == "0" ? "5" : v === "2" ? "0" : "2").join("");
}