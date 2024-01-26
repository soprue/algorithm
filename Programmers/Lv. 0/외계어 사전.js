function solution(spell, dic) {
    for(let x of dic) {
        if([...x].sort().join() == spell.sort().join()) return 1;
    }
    return 2;
}