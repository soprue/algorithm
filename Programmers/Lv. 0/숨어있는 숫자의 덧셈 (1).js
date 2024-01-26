function solution(my_string) {
  return [...my_string].filter((v) => !isNaN(v)).reduce((acc, cur) => acc += Number(cur), 0);
}