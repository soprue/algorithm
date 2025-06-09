/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
var sortedArrayToBST = function(nums) {
    const buildTree = (left, right) => {
        if(left > right) return null; // 범위가 없으면 트리도 없음

        const mid = Math.floor((left + right) / 2);
        const node = new TreeNode(nums[mid]); // 중간값으로 노드 만들기

        node.left = buildTree(left, mid - 1); // 왼쪽 절반으로 왼쪽 서브트리 만들기
        node.right = buildTree(mid + 1, right); // 오른쪽 절반으로 오른쪽 서브트리 만들기

        return node;
    }

    return buildTree(0, nums.length - 1);
};
