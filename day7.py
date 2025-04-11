class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def searchBST(self, root, val):
        if root is None:
            return None
        if root.val==val :
            return root
        if val<root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

obj = Solution()
result = obj.searchBST(root, 4)

