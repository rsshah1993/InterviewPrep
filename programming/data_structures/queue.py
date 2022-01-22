from typing import Optional, Any


class Node:
    def __init__(self, head: Any, next: Optional['Node'] = None):
        self.head = head
        self.next = next

    def get_list(self):
        output = [self.head]

        node = self.next
        while node:
            output.append(node.head)
            node = node.next

        return output

    def __str__(self):
        output = self.get_list()
        return f"{output}"


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, val: int) -> None:
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node

        self.size += 1
        self.tail = node

    def pop(self):
        if self.is_empty():
            raise ValueError("Queue is empty!")

        temp = self.head
        self.head = self.head.next
        self.size -= 1

        if self.head is None:
            self.tail = None

        return temp.head

    def is_empty(self):
        return self.size == 0


if __name__ == "__main__":
    queue = Queue()
    for i in range(10):
        queue.push(i)
        print(queue.head)

    for i in range(10):
        queue.pop()
        print(queue.tail)
