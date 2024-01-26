function solution(dots) {
    let xDots = dots.map(([x, y]) => x);
    let yDots = dots.map(([x, y]) => y);
    let width = Math.max(...xDots) - Math.min(...xDots);
    let height = Math.max(...yDots) - Math.min(...yDots);
    
    return width * height;
}