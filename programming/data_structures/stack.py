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


class Stack:
    def __init__(self):
        self._stack = Node("head")
        self._top = 0

    def __str__(self):
        return str(self._stack.get_list()[::-1])

    def push(self, elem: int):
        node = Node(elem)
        node.next = self._stack.next
        self._stack.next = node
        self._top += 1

    def pop(self):
        remove = self._stack.next
        self._stack.next = self._stack.next.next
        self._top -= 1
        return remove.head

    def top(self):
        return self._top

    def is_empty(self):
        return self._top < 1


if __name__ == "__main__":
    stack = Stack()
    print(f"Stack is empty: {stack.is_empty()}")
    for i in range(10):
        print(f'Pushing {i} to stack')
        stack.push(i)
        print(f"Stack looks like: {stack.__str__()}")

    print(f"\nStack is empty: {stack.is_empty()}\n")

    while not stack.is_empty():
        k = stack.pop()
        print(f"Stack has {stack.top()} elements remaining with {k} on top")
        print(f"Stack looks like: {stack.__str__()}")
