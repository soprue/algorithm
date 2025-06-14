/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
    // 둘 다 null이면 같음 (끝까지 잘 비교했단 뜻)
    if (p === null && q === null) return true;

    // 한쪽만 null이거나, 값이 다르면 다름
    if (p === null || q === null || p.val !== q.val) return false;

    // 왼쪽 & 오른쪽 자식 노드도 각각 비교
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
};
