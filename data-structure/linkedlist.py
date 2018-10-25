class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        node = Node(value)

        if not self.head:
            self.head = node
            self.tail = node
        else:
            prev = self.tail
            prev.next = node

            self.tail = node

    def print(self):
        node = self.head
        while node:
            print(node.value, end=' > ')
            node = node.next


def main():

    l = LinkedList()
    l.add(1)
    l.add(3)
    l.add(2)
    l.add(9)
    l.add(7)

    l.print()


if __name__ == '__main__':
    main()
