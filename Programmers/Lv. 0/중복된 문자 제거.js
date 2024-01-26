function solution(my_string) {
    return [...my_string].filter((ele, idx) => my_string.indexOf(ele) == idx).join("");
}