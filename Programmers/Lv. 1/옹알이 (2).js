function solution(babbling) {
    let words = ["aya", "ye", "woo", "ma"];
    
    return babbling.filter((v) => {
        words.forEach((word) => {
            v = v.replace(new RegExp(word + word, "gi"), "cannot");
            v = v.replace(new RegExp(word, "gi"), "1");
        });
        return v.replace(new RegExp("1", "g"), "") == "";
    }).length;
}