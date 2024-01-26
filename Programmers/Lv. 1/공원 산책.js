
const DIR = { E: [0, 1], W: [0, -1], S: [1, 0], N: [-1, 0] };

function solution(park, routes) {
    let robot = [];
    
    let width = park[0].length - 1;
    let height = park.length - 1;
    
    for(let i=0; i<park.length; i++) {
        if(park[i].indexOf("S") > -1) {
            robot = [i, park[i].indexOf("S")];
            break;
        }
    }

    routes.forEach((route) => {
        let [dir, count] = route.split(" ");
        let [nx, ny] = [...robot];
        
        let cnt = 0;
        while (cnt < count) {
            [nx, ny] = [nx + DIR[dir][0], ny + DIR[dir][1]];
            if (!park[nx] || !park[nx][ny] || park[nx][ny] === "X") break;
            cnt++;
        }
        
        if (cnt == count) robot = [nx, ny];
    });
    
    return robot;
}
