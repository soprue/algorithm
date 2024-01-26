function solution(str1, str2) {
    const explode = (str) => {
        let result = [];
        
        for(let i=0; i<str.length - 1; i++) {
            let ele = (str[i] + str[i + 1]).toUpperCase();
            if(/^[a-zA-Z]+$/.test(ele)) result.push(ele);
        }
        
        return result;
    }
    
    let arr1 = explode(str1);
    let arr2 = explode(str2);
    
    const set = new Set([...arr1, ...arr2]);
    let union = 0;
    let intersection = 0;

    set.forEach(item => {
        const has1 = arr1.filter(x => x === item).length;
        const has2 = arr2.filter(x => x === item).length;
        union += Math.max(has1, has2);
        intersection += Math.min(has1, has2);
    });
    
    return union ? parseInt(intersection / union * 65536) : 65536;
}

// https://school.programmers.co.kr/learn/courses/30/lessons/17677
// 위 풀이는 문제 본문에 언급된 Math.max()와 Math.min()을 사용해서 풀이
// 근데 안 쓰고 밑처럼 푸는 게 더 빠름...

// function solution(str1, str2) {
//     const explode = (str) => {
//         let result = [];
        
//         for(let i=0; i<str.length - 1; i++) {
//             let ele = (str[i] + str[i + 1]).toUpperCase();
//             if(/^[a-zA-Z]+$/.test(ele)) result.push(ele);
//         }
        
//         return result;
//     }
    
//     let arr1 = explode(str1);
//     let arr2 = explode(str2);
    
//     // 교집합 개수 세기
//     const arr3 = [...arr2];
//     let intersection = 0;
//     arr1.forEach((ele, idx) => {
//         for(let i = 0; i < arr3.length; i++) {
//             if (ele === arr3[i]) {
//                 arr3.splice(i, 1);
//                 intersection++;
//                 break;
//             }
//         }
//     });
    
//     const union = arr1.length + arr2.length - intersection;
    
//     return union ? parseInt(intersection / union * 65536) : 65536;
// }
