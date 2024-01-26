function solution(id_list, report, k) {
    const reportResult = report.reduce((acc, cur) => {
        const [user, reported] = cur.split(' ');
        acc[reported] = acc[reported] ? acc[reported].add(user) : new Set().add(user);
        return acc;
    }, {});

    const mailed = Object.values(reportResult)
        .filter(set => set.size >= k)
        .flatMap(set => [...set]);
    
    return id_list.map(id => mailed.filter(user => user === id).length);
}