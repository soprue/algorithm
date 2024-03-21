# https://www.acmicpc.net/problem/1991

import sys
 
N = int(sys.stdin.readline().strip())
tree = {}
 
for n in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]
 
# (루트) (왼쪽 자식) (오른쪽 자식)
def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])
 
# (왼쪽 자식) (루트) (오른쪽 자식)
def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])
 
# (왼쪽 자식) (오른쪽 자식) (루트)
def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

rootNode = 'A'
preorder(rootNode)
print()
inorder(rootNode)
print()
postorder(rootNode)
