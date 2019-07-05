class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def printlist(self):
        temp = self.head
        while(temp.next != None):
            print(temp.data, end='-->')
            temp = temp.next
        print(temp.data)

    def addAtStart(self, element):
        if self.head is not None and type(element) is type(self.head.data):
            temp = Node(element)
            temp.next = self.head
            self.head = temp

        else:
            if self.head is None:
                self.head = Node(element)
            else:
                raise Exception(
                    'The element must be of  '+str(type(self.head.data)))

    def addAtEnd(self, element):
        if self.head is not None and type(element) is type(self.head.data):
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = Node(element)

        else:
            if self.head is None:
                self.head = Node(element)
            else:
                raise Exception(
                    'The element must be of type '+str(type(self.head.data)))


def main():

    ls = LinkedList()
    ls.addAtEnd(5)
    ls.addAtEnd(2)
    ls.addAtEnd(4)
    ls.printlist()


if __name__ == '__main__':
    main()
