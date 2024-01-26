function solution(cacheSize, cities) {
    const MISS = 5, HIT = 1;
    
    if(cacheSize == 0) return cities.length * MISS;
    
    let answer = 0;
    let cache = [];
    
    cities.forEach(city => {
        city = city.toLowerCase();
        
        let index = cache.indexOf(city);
        if(index >= 0) {
            cache.splice(index, 1);
            answer += HIT;
        } else {
            if(cache.length == cacheSize) cache.shift();
            answer += MISS;
        }
        
        cache.push(city);
    });
    
    return answer;
}
