from LinkedList import DoubleLinkedList


class Queue:
    def __init__(self):
        self.__list = DoubleLinkedList()

    def enqueue(self, val):
        self.__list.add(val)

    def dequeue(self):
        val = self.__list.front()
        self.__list.remove_fast()
        return val

    def front(self):
        self.__list.front()

    def __len__(self):
        return self.__list.size

    def is_empty(self):
        return self.__list.size == 0