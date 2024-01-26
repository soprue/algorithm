function solution(sizes) {
    let wMax = 0, hMax = 0;
    sizes.map(v => { 
        const [a, b] = v.sort((a,b) => a - b);
        wMax = Math.max(v[0], wMax);
        hMax = Math.max(v[1], hMax);
    });
    return wMax * hMax;
}