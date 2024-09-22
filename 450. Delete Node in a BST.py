'''
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
 

Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
Example 3:

Input: root = [], key = 0
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-105 <= Node.val <= 105
Each node has a unique value.
root is a valid binary search tree.
-105 <= key <= 105
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestDescendant(self, root):
        while root.left:
            root = root.left
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        else:
            # Checks for Lesser value
            if root.val > key:
                root.left = self.deleteNode(root.left, key)
            # Checks for Greater value
            elif root.val < key:
                root.right = self.deleteNode(root.right, key)
            # Checks if we have reached the node we want to delete
            else:
                # First we check if only 1 child node is present
                if not root.left:
                    root = root.right
                elif not root.right:
                    root = root.left
                else:
                # If both the children are present then we find the
                # smallest child in the right child and assign it's
                # value to node and recursively delete that child 
                # until we have reach node with 1 child or leaf node
                    temp = self.smallestDescendant(root.right)
                    root.val = temp.val
                    root.right = self.deleteNode(root.right, temp.val)
            return root