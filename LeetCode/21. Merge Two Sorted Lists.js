/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    const answer = new ListNode();
    let current = answer;

    while (list1 && list2) {
        // 더 작은 노드를 결과에 붙이고, 그 리스트 한 칸 이동
        if (list1.val < list2.val) {
            current.next = list1;
            list1 = list1.next;
        } else {
            current.next = list2;
            list2 = list2.next;
        }
        current = current.next; 
    }
    
    current.next = list1 || list2; // 남은 노드 한 줄로 이어 붙이기

    return answer.next;  
};
