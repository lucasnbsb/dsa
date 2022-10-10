from re import search


class TreeNode:
    def __init__(self, val):
        self.val = val;
        self.left = None
        self.right = None

# left is always less
# right is always greater
# O(h), O(log n) for a balanced tree
class BST:
    def search(root, target):
        if not root:
            return False
        
        if target > root.val:
            return search(root.right, target)
        elif target < root.val: 
            return search(root.left, target)
        else:
            return True


    # Insert a new node and return the root of the BST.
    def insert(root, val):
        if not root:
            return TreeNode(val)
        
        if val > root.val:
            root.right = insert(root.right, val)
        elif val < root.val:
            root.left = insert(root.left, val)
        return root

    # Return the minimum value node of the BST.
    def minValueNode(root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    # Remove a node and return the root of the BST. 2*log(n)
    def remove(root, val):
        if not root:
            return None
        
        if val > root.val:
            root.right = remove(root.right, val)
        elif val < root.val:
            root.left = remove(root.left, val)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = minValueNode(root.right)
                root.val = minNode.val
                root.right = remove(root.right, minNode.val)
        return root
