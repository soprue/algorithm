function solution(clothes) {
    let answer = 1;
    let closet = {};
    
    clothes.forEach(v => {
        let [name, category] = v;
        
        if (closet[category] === undefined) {
            closet[category] = [name];
        } else {
            closet[category].push(name);
        }
    });

    for (const [key, value] of Object.entries(closet)) {
        // 해당 종류의 의상을 안 입는 경우도 있을 수 있기 때문에 의상 개수에 1을 더한 값을 곱함 
        answer *= (value.length + 1);
    }
    // 최소 한 개의 의상은 입어야 하니 모든 의상을 안 입는 경우를 빼 줘야 함
    return answer - 1;
}
