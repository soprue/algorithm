function solution(bandage, health, attacks) {
    const [time, recovery, bonusRecovery] = bandage;
    let leftHealth = health;
    let recentAttack = 0; // 최근 공격 시간
    
    for (const [attackTime, attackDamage] of attacks) {
        // 공격 시간에 도달하기 전까지 '붕대 감기' 시전
        const timeDiff = attackTime - recentAttack - 1;
        const success = Math.floor(timeDiff / time); // 공격 시간 차를 시전 시간으로 나누고 소수점을 버리면 연속 성공 횟수
        const totalRecovery = (timeDiff * recovery) + (success * bonusRecovery);
        leftHealth = leftHealth + totalRecovery >= health ? health : leftHealth + totalRecovery;
        
        // 공격
        leftHealth -= attackDamage;
        if (leftHealth <= 0) return -1;
        
        // 최근 공격 시간을 업데이트 해주고 다시 순환 시작
        recentAttack = attackTime;
    }
    
    return leftHealth;
}
