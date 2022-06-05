from LinkedList import DoubleLinkedList


class Stack:
    def __init__(self):
        self.__list = DoubleLinkedList()

    def push(self, val):
        self.__list.add(val)

    def pop(self):
        val = self.__list.back()
        self.__list.remove_last()
        return val

    def is_empty(self):
        return self.__list.size == 0

    def peek(self):
        return self.__list.back()

    def __len__(self):
        return self.__list.size


my_stack = Stack()

my_stack.push(5)
my_stack.push(6)
my_stack.push(7)
my_stack.push(8)

print(len(my_stack))
print(my_stack.pop())
print(my_stack.peek())
