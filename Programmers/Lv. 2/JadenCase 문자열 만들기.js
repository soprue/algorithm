function solution(s) {
    let arr = s.split(" ");
    return arr.map((v, idx) => {
        return v.charAt(0).toUpperCase() + v.substring(1).toLowerCase();
    }).join(" ");
}
