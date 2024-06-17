function solution(tickets) {
    const routes = {};
    tickets.forEach(([from, to]) => {
        if (!routes[from]) routes[from] = [];
        routes[from].push(to);
    });
    
    for (const key in routes) {
        routes[key].sort();
    }
    
    const stack = ["ICN"], path = [];
    
    while(stack.length > 0) {
        let top = stack[stack.length - 1];
        if (routes[top] && routes[top].length > 0) {
            stack.push(routes[top].shift());
        } else {
            path.push(stack.pop());
        }
    }
    
    return path.reverse();
} 
