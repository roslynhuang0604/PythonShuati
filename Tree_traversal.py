
class Solution(object):
"""
Pre Order
（1） root 放入stack
（2） pop一个element，打印，放右孩子，左孩子
（3） repeat while stack is not empty
"""

    def preorderIterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        stack = [root] # root might be None
        while stack:
            cur = stack.pop()
            if cur:
                ret.append(cur.val)
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
        return ret

    def preorderRecursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        self.recurHelper(root, ret)
        return ret

    def recurHelper(self, root, ret):
        if root is None:
            return
        ret.append(root.val)
        self.recurHelper(root.left, ret)
        self.recurHelper(root.right, ret)

"""
In Order
（1） 只要有左孩子，把所有左孩子压入stack
（2） 没有左孩子，pop一个，let cur = cur.right
（3） repeat while cur or stack

"""
    def inorderIterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret, stack = [], []
        cur = root # root might be None
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                ret.append(cur.val)
                cur = cur.right
        return ret


    def inorderRecursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        self.recurHelper(root, ret)
        return ret

    def recurHelper(self, root, ret):
        if root is None:
            return
        self.recurHelper(root.left, ret)
        ret.append(root.val)
        self.recurHelper(root.right, ret)

"""
Post Order
post-order is the reverse order of pre-order with traversaling right subtree
before the left subtree

     1
    / \
   2   3
  / \  / \
 4  5  6  7
 preorder = 1245367 stack = [132 54 76] ret = [1245367]
                              ||  |  |
                              rl  l  r
            先放right,再放left so that you visit left subtree first

 postorder = 4526731 stack = [123 67 45] ret = [1376254]->[4526731]
                               ||  |  |
                               lr  r  l
            先放right,再放left so that you visit left subtree first

"""

    def postorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    ret = []
    stack = [root]
    while stack:
        cur = stack.pop()
        if cur:
            ret.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
    ret.reverse() # reverse in-place O(n)
    return ret
