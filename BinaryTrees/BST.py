class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def find_minimun_in_tree(self, root):
        if root.left == None:
            return root
        return self.find_minimun_in_tree(root.left)

    def __init__(self, root=None):
        self.root = root

    def addElement(self, data):
        node = Node(data)

        if self.root is None:
            self.root = node
        else:
            temp = self.root

            while(temp is not None):

                if(data < temp.data):
                    temp = temp.left
                else:
                    temp = temp.right

            temp = node

    def deleteElement(self, root, data, prev):

        if data < root.data:
            self.deleteElement(root.left, data, root)
            return

        elif data > root.data:
            self.deleteElement(root.right, data, root)
            return
        else:

            if root.right is None and root.left is None:
                root = None
            elif root.right is None:
                prev.left = root.right
                root = None

            elif root.left is None:
                prev.right = root.left
                root = None
            else:
                temp = self.find_minimun_in_tree(root.right)
                root = temp
                temp = None

            return

    def printTree(self):
