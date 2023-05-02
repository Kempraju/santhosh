# Implement Binary tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # Traverse preorder
    def traversePreOrder(self):
        print(self.val, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    # Traverse inorder
    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.val, end=' ')
        if self.right:
            self.right.traverseInOrder()

    # Traverse postorder
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.val, end=' ')


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)

print("Pre order Traversal: ", end="")
root.traversePreOrder()
print("\nIn order Traversal: ", end="")
root.traverseInOrder()
print("\nPost order Traversal: ", end="")
root.traversePostOrder()

# Find height of a given tree

class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Compute the "maxDepth" of a tree -- the number of nodes
# along the longest path from the root node down to the
# farthest leaf node


def maxDepth(node):
    if node is None:
        return 0

    else:

        # Compute the depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)

        # Use the larger one
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print("Height of tree is %d" % (maxDepth(root)))

# Perform Pre-order, Post-order, In-order traversal

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A function to do inorder tree traversal
def printInorder(root):

    if root:

        # First recur on left child
        printInorder(root.left)

        # then print the data of node
        print(root.val),

        # now recur on right child
        printInorder(root.right)


# Driver code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Function call
    print ("\nInorder traversal of binary tree is")
    printInorder(root)

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A function to do preorder tree traversal
def printPreorder(root):

    if root:

        # First print the data of node
        print(root.val),

        # Then recur on left child
        printPreorder(root.left)

        # Finally recur on right child
        printPreorder(root.right)


# Driver code
if __name__ == "__main__":
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  root.left.left = Node(4)
  root.left.right = Node(5)

  # Function call
  print ("Preorder traversal of binary tree is")
  printPreorder(root)

  class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# A function to do postorder tree traversal
def printPostorder(root):

    if root:

        # First recur on left child
        printPostorder(root.left)

        # the recur on right child
        printPostorder(root.right)

        # now print the data of node
        print(root.val),


# Driver code
if __name__ == "__main__":
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  root.left.left = Node(4)
  root.left.right = Node(5)

  # Function call
  print ("\nPostorder traversal of binary tree is")
  printPostorder(root)

  #Function to print all the leaves in a given binary tree
  class Node:
    # constructor to create tree node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# function to print all path from root
# to leaf in binary tree
def printPaths(root):
    # list to store path
    path = []
    printPathsRec(root, path, 0)

# Helper function to print path from root
# to leaf in binary tree
def printPathsRec(root, path, pathLen):

    # Base condition - if binary tree is
    # empty return
    if root is None:
        return

    # add current root's data into
    # path_ar list

    # if length of list is gre
    if(len(path) > pathLen):
        path[pathLen] = root.data
    else:
        path.append(root.data)

    # increment pathLen by 1
    pathLen = pathLen + 1

    if root.left is None and root.right is None:

        # leaf node then print the list
        printArray(path, pathLen)
    else:
        # try for left and right subtree
        printPathsRec(root.left, path, pathLen)
        printPathsRec(root.right, path, pathLen)

# Helper function to print list in which
# root-to-leaf path is stored
def printArray(ints, len):
    for i in ints[0 : len]:
        print(i," ",end="")
    print()

# Driver program to test above function
"""
Constructed binary tree is
            10
        / \
        8     2
    / \ /
    3 5 2
"""
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)
printPaths(root)

# Implement BFS (Breath First Search) and DFS (Depth First Search)
import collections

# BFS algorithm
def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)

# DFS algorithm
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

dfs(graph, '0')

# Find sum of all left leaves in a given Binary Tree

class Node:

    # A constructor to create a new Node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def leftLeavesSumRec(root, isLeft, summ):
    if root is None:
        return

    # Check whether this node is a leaf node and is left
    if root.left is None and root.right is None and isLeft == True:
        summ[0] += root.key

    # Pass 1 for left and 0 for right
    leftLeavesSumRec(root.left, 1, summ)
    leftLeavesSumRec(root.right, 0, summ)


# A wrapper over above recursive function
def leftLeavesSum(root):
    summ = [0] # initialize result

    # Use the above recursive function to evaluate sum
    leftLeavesSumRec(root, 0, summ)

    return summ[0]

# Driver program to test above function

# Let us construct the Binary Tree shown in the
# above figure
root = Node(20);
root.left= Node(9);
root.right   = Node(49);
root.right.left = Node(23);
root.right.right= Node(52);
root.right.right.left  = Node(50);
root.left.left  = Node(5);
root.left.right = Node(12);
root.left.right.right  = Node(12);

print ("Sum of left leaves is", leftLeavesSum(root))

# Find sum of all nodes of the given perfect binary tree
def SumNodes(l):

    # no of leaf nodes
    leafNodeCount = pow(2, l - 1)

    # list of vector to store nodes of
    # all of the levels
    vec = [[] for i in range(l)]

    # store the nodes of last level
    # i.e., the leaf nodes
    for i in range(1, leafNodeCount + 1):
        vec[l - 1].append(i)

    # store nodes of rest of the level
    # by moving in bottom-up manner
    for i in range(l - 2, -1, -1):
        k = 0

        # loop to calculate values of parent nodes
        # from the children nodes of lower level
        while (k < len(vec[i + 1]) - 1):

            # store the value of parent node as
            # Sum of children nodes
            vec[i].append(vec[i + 1][k] +
                          vec[i + 1][k + 1])
            k += 2

    Sum = 0

    # traverse the list of vector
    # and calculate the Sum
    for i in range(l):
        for j in range(len(vec[i])):
            Sum += vec[i][j]

    return Sum

# Driver Code
if __name__ == '__main__':
    l = 3

    print(SumNodes(l))

# Count subtress
#  that sum up to a given value x in a binary tree
class Node:
    def __init__(self):
        self.data = 0;
        self.left = None;
        self.right = None;

# Function to get a new Node
def getNode(data):

    # Allocate space
    newNode = Node();

    # Put in the data
    newNode.data = data;
    newNode.left = newNode.right = None;
    return newNode;

# Function to find digit sum of number
def digitSum(N):
    sum = 0;
    while (N > 0):
        sum += N % 10;
        N //= 10;

    return sum;

# Function to replace all the Nodes
# with their digit sums using pre-order
def replaceNodes(root):
    if (root == None):
        return;

    # Assigning digit sum value
    root.data = digitSum(root.data);

    # Calling left sub-tree
    replaceNodes(root.left);

    # Calling right sub-tree
    replaceNodes(root.right);


# Function to count subtrees that
# Sum up to a given value x
def countSubtreesWithSumX(root, x):

    # If tree is empty
    if (root == None):
        return 0;

    # Sum of Nodes in the left subtree
    ls = countSubtreesWithSumX(root.left,  x);

    # Sum of Nodes in the right subtree
    rs = countSubtreesWithSumX(root.right,  x);

    # Sum of Nodes in the subtree rooted
    # with 'root.data'
    sum = ls + rs + root.data;

    # If True
    if (sum == x):
        count += 1;

    # Return subtree's Nodes sum
    return sum;


# Utility function to count subtrees that
# sum up to a given value x
def countSubtreesWithSumXUtil(root, x):

    # If tree is empty
    if (root == None):
        return 0;

    count = 0;

    # Sum of Nodes in the left subtree
    ls = countSubtreesWithSumX(root.left,  x);

    # sum of Nodes in the right subtree
    rs = countSubtreesWithSumX(root.right,  x);

    # If tree's Nodes sum == x
    if ((ls + rs + root.data) == x):
        count+=1;

    # Required count of subtrees
    return count;

# Driver program to test above
if __name__ == '__main__':
    N = 7;
    '''Binary tree creation
           10         
          /   \
        2       3
      /  \     /  \  
     9    3    4   7'''
    root = getNode(10);
    root.left = getNode(2);
    root.right = getNode(3);
    root.left.left = getNode(9);
    root.left.right = getNode(3);
    root.right.left = getNode(4);
    root.right.right = getNode(7);

    # Replacing Nodes with their
    # digit sum value
    replaceNodes(root);

    X = 29;

    print(countSubtreesWithSumXUtil(root, X))

# Find maximum level sum in Binary Tree
from collections import deque

# A binary tree node has data, pointer
# to left child and a pointer to right
# child
class Node:

    def __init__(self, key):

        self.data = key
        self.left = None
        self.right = None

# Function to find the maximum sum
# of a level in tree
# using level order traversal
def maxLevelSum(root):

    # Base case
    if (root == None):
        return 0

    # Initialize result
    result = root.data

    # Do Level order traversal keeping
    # track of number
    # of nodes at every level.
    q = deque()
    q.append(root)

    while (len(q) > 0):

        # Get the size of queue when the
        # level order traversal for one
        # level finishes
        count = len(q)

        # Iterate for all the nodes in
        # the queue currently
        sum = 0
        while (count > 0):

            # Dequeue an node from queue
            temp = q.popleft()

            # Add this node's value to current sum.
            sum = sum + temp.data

            # Enqueue left and right children of
            # dequeued node
            if (temp.left != None):
                q.append(temp.left)
            if (temp.right != None):
                q.append(temp.right)

            count -= 1   

        # Update the maximum node count value
        result = max(sum, result)

    return result

# Driver code
if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(8)
    root.right.right.left = Node(6)
    root.right.right.right = Node(7)

    # Constructed Binary tree is:
    #              1
    #            /   \
    #          2      3
    #        /  \      \
    #       4    5      8
    #                 /   \
    #                6     7   
    print("Maximum level sum is", maxLevelSum(root))

# Print the nodes at odd levels of a tree

class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def printOddNodes(root, isOdd = True):

    # If empty tree
    if (root == None):
        return

    # If current node is of odd level
    if (isOdd):
        print(root.data, end = " ")

    # Recur for children with isOdd
    # switched.
    printOddNodes(root.left, not isOdd)
    printOddNodes(root.right, not isOdd)

# Driver code
if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    printOddNodes(root)
