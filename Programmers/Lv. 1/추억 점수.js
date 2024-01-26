function solution(name, yearning, photo) {
    return photo.map(v => {
        return v.reduce((a, c) => a += yearning[name.indexOf(c)] ?? 0, 0);
    });
}
