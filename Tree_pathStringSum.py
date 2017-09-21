'''
Given a binary tree, sum all of the numbers created by the paths from the root to each leaf.

For example, the tree below has the following paths:
		       1
                      /   \
                     /     \
                    4       5
                   / \
                  3   7
                       \
                        9

1->4->3, which creates the number 143. 1->4->7->9, which creates the number 1479. 1->5, which creates the number 15.

The sum for this tree is 143 + 1479 + 15 = 1637.

'''

import unittest

class TestSumPaths(unittest.TestCase):

  def testSanity(self):
    n1 = Node(value=1)
    self.assertEqual(n1.sumPaths(), 1)

  # Write some more test cases
  def test1(self):
      root = Node(value = 1)
      root.left = Node(value = 2)
      root.right = Node(value = 3)
      self.assertEqual(root.sumPaths(), 25)

  def test2(self):
      root = Node(value = 1)
      n1 = Node(value = 12)
      n2 = Node(value = 5)
      n3 = Node(value = 31)

      root.left = n1
      root.right = n2
      n2.right = n3
      self.assertEqual(root.sumPaths(), 1643)

  def test3(self):
      root = Node(value = 0)
      n1 = Node(value = 0)
      n2 = Node(value = 0)
      n3 = Node(value = 0)

      root.left = n1
      root.right = n2
      n2.right = n3
      self.assertEqual(root.sumPaths(), 0)



class Node:
  result = []
  def __init__(self, value=0, left=None, right=None):
    self.left = left
    self.right = right
    self.value = value

  def sumPaths(self):
    # path: used to store single path sum
    # result: used to store all the single path sums
    path, result = [], []
    self.sumPathsRecu(path, result)

    # sum all the strings in the result list
    return sum(int(i) for i in result)


  def sumPathsRecu(self, path, result):
      if self is None:
        return

      # if we reach the leaf nodes, sum the entir path and append the sum to the result list
      if(self.left == None and self.right == None):
        sol = ""
        for num in path:
          sol += str(num.value)
        sol += str(self.value)
        result.append(sol)

      # if left child is not None, recurse down
      if self.left:
        path.append(self)
        self.left.sumPathsRecu(path, result)
        path.pop()

      # if right child is not None, recurse down
      if self.right:
        path.append(self)
        self.right.sumPathsRecu(path, result)
        path.pop()

if __name__ == "__main__":
  unittest.main()
