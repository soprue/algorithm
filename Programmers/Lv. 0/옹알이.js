function solution(babbling) {
    const words = ["aya", "ye", "woo", "ma"]
    return babbling.filter((v) => {
        words.forEach((word) => {
            v = v.replace(new RegExp(word + word, 'gi'), 'cannot')
            v = v.replace(new RegExp(word, 'gi'), '')
        })
        return v === '';
    }).length;
}
