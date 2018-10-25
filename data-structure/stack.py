class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        pop_value = self.stack_list.pop()
        print('POP >> ', pop_value)

        return pop_value

    def print(self):
        print('=========== TOP')
        for v in reversed(self.stack_list):
            print(v)
        print('=========== BOTTOM')


def main():
    stack = Stack()

    stack.push(1)
    stack.push(3)
    stack.push(2)
    stack.push(9)

    stack.print()

    stack.pop()
    stack.pop()

    stack.print()


if __name__ == '__main__':
    main()
