/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var sortList = function(head) {
    if (!head || !head.next) return head;

    let slow = head; // 한 칸씩 이동
    let fast = head; // 두 칸씩 이동
    let prev = null; // slow 바로 전 노드 기억용

    // 중간 찾기
    while (fast && fast.next) {
        prev = slow;
        slow = slow.next;
        fast = fast.next.next;
    }
    prev.next = null; // 리스트를 반으로 자름

    const left = sortList(head);
    const right = sortList(slow); 

    return merge(left, right);
};

function merge(l1, l2) {
    let dummy = new ListNode(0); // 정렬 결과를 만들 임시 노드
    let current = dummy; // 현재 결과 리스트에서 끝부분을 가리키는 포인터

    while (l1 && l2) {
        // 값 비교해서 더 작은 쪽 연결
        if (l1.val < l2.val) {
            current.next = l1;
            l1 = l1.next;
        } else {
            current.next = l2;
            l2 = l2.next;
        }
        current = current.next;
    }

    current.next = l1 || l2;
    return dummy.next;
}
