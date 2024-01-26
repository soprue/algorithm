function solution(numbers, k) {
  let current = 0;
  const goNext = current => (current + 2) % numbers.length;
  for (let i = 0; i < k - 1; i++) current = goNext(current);
  return numbers[current];
}