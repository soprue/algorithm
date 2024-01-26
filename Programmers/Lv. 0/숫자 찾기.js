function solution(num, k) {
    let index = [...(num+"")].indexOf(k + "");
    return index == -1 ? -1 : index + 1;
}