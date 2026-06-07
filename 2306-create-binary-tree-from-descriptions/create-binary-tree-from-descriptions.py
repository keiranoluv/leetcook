# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()

        for parent, child, isLeft in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)
            
            parent_node = nodes[parent]
            child_node = nodes[child]

            if isLeft==1:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
            
            children.add(child)

        for val in nodes:
            if val not in children:
                return nodes[val]
            
    