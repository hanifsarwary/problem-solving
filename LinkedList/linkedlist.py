class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self, head):
        self.head = head

    def printlist(self):
        temp = self.head
        while(temp != None):
            print(temp.data)
            temp = temp.next

    def addAtStartElement(self, element):
        element.next = self.head
        self.head = element


def main():

    head = Node(5)
    e1 = Node(4)

    ls = LinkedList(head)
    ls.addAtStartElement(e1)
    ls.printlist()


if __name__ == '__main__':
    main()
