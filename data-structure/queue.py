class Queue:
    def __init__(self):
        self.queue_list = []

    def enqueue(self, value):
        self.queue_list.append(value)

    def dequeue(self):
        dequeue_value = self.queue_list.pop(0)
        print('DEQUEUE >>', dequeue_value)

        return dequeue_value

    def print(self):
        print('FRONT ====>>>>>>==== REAR')
        for v in self.queue_list:
            print(v, end=' ')
        print()


def main():
    stack = Queue()

    stack.enqueue(1)
    stack.enqueue(3)
    stack.enqueue(2)
    stack.enqueue(9)

    stack.print()

    stack.dequeue()
    stack.dequeue()

    stack.print()


if __name__ == '__main__':
    main()
