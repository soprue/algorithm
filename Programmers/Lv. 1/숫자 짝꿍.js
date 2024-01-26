function solution(X, Y) {
    let result = "";
    const map = new Map();
    
    for(let i = 0; i < X.length; i++){
        map.set(X[i], (map.get(X[i]) || 0) + 1);
    }

    for(let i = 0; i < Y.length; i++){
        if(map.get(Y[i]) >= 1){
            map.set(Y[i], map.get(Y[i]) - 1)
            result += Y[i];
        }
    }
    
    if(result.length < 1) return "-1";
    return +result === 0 ? "0" : result.split("").sort((a, b) => b - a).join("");
}