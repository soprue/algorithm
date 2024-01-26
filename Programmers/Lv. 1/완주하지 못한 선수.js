function solution(participant, completion) {
    let hMapComp = new Map();
    let hMapPart = new Map();

    for (let comp of completion) {
        hMapComp.set(comp, hMapComp.get(comp) ? hMapComp.get(comp) + 1 : 1);
    }
    for (let part of participant) {
        hMapPart.set(part, hMapPart.get(part) ? hMapPart.get(part) + 1 : 1);
    }

    for (let part of participant) {
        if (hMapPart.get(part) !== hMapComp.get(part)) return part;
    }
}