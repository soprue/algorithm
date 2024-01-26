function solution(wallpaper) {
    let lux, luy, rdx, rdy;
    
    const files = [];
    for (let i = 0; i < wallpaper.length; i++) {
        for (let j = 0; j < wallpaper[i].length; j++) {
            if ("#" === wallpaper[i][j]) {
                files.push([i, j]);
            }
        }
    }

    files.forEach((file) => {
        lux = lux >= 0 ? Math.min(lux, file[0]) : file[0];
        luy = luy >= 0 ? Math.min(luy, file[1]) : file[1];
        rdx = rdx >= 0 ? Math.max(rdx, file[0]) : file[0];
        rdy = rdy >= 0 ? Math.max(rdy, file[1]) : file[1];
    })

    
    return [lux, luy, rdx + 1, rdy + 1];
}
