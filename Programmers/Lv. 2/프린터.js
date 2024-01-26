function solution(priorities, location) {
    let list = priorities.map((v, idx) => {
       return {
            mine: idx === location,
            val: v
       };
    });
    
    let count = 0;
    
    while(true) {
        let current = list.shift();        
        if(list.some(v => v.val > current.val)) {
            list.push(current);                        
        } else {            
            count++;
            if(current.mine) return count;
        }
    }
}
