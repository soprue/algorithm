
function solution(today, terms, privacies) {
    today = Number(today.replace(/\./g, ""));
    
    let termsMap = {};
    terms.map((v) => {
        let [type, month] = v.split(" ");
        termsMap[type] = Number(month);
    });
    
    let answer = [];
    privacies.forEach((v, idx) => {
        let [date, type] = v.split(" ");
        let [y, m, d] = date.split(".").map(Number);
        
        // 파기 일자 구하기
        m += termsMap[type];
        while(m > 12){
            y += 1;
            m -= 12;
        }
        
        y = String(y);
        m = String(m).padStart(2, "0");
        d = String(d).padStart(2, "0");
        let expirationDate = Number(y + m + d);
        
        if(today >= expirationDate) answer.push(idx + 1);
    });
    
    return answer;
}