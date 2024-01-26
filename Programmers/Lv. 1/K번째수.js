function solution(array, commands) {
    return commands.map(([start, end, pos] = v) => {
        return array.slice(start - 1, end)
                    .sort((a, b) => a - b)[pos - 1];
    });
}