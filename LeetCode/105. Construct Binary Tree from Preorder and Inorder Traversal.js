/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function(preorder, inorder) {
    // 전위 순회에서는 첫 번째 인덱스가 루트
    // 중위 순회에서 루트 찾기 -> 그 기준 왼쪽이 왼쪽 노드, 오른쪽이 오른쪽 노드

    // 나중에 root 값을 기준으로 inorder에서 왼쪽/오른쪽 구간을 빠르게 찾기 위해 사용
    const inorderMap = new Map();
    for (let i = 0; i < inorder.length; i++) {
        inorderMap.set(inorder[i], i);
    }

    let preorderIndex = 0;

    function helper(left, right) {
        if (left > right) return null;

        const rootVal = preorder[preorderIndex++];
        const root = new TreeNode(rootVal);

        const mid = inorderMap.get(rootVal);

        root.left = helper(left, mid - 1);
        root.right = helper(mid + 1, right);

        return root;
    }

    return helper(0, inorder.length - 1);
};
