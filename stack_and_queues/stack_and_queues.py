from .exceptions import EmptyStack


class StackMin:
    """
    Q. 3.2
    Stack with min function in O(1)
    """

    def __init__(self):
        self._stack = []  # implement a stack using an array
        self._min_stack = []  # stack for min values

    def check_empty_stack(self):
        if self.is_empty():
            raise EmptyStack("Stack is empty")

    def min(self):
        self.check_empty_stack()
        return self._min_stack[-1]

    def push(self, value):
        if not self._min_stack or self._min_stack[-1] > value:
            self._stack.append(value)
            self._min_stack.append(value)
        else:
            self._stack.append(value)

    def is_empty(self) -> bool:
        return not self._stack

    def peek(self):
        self.check_empty_stack()
        return self._stack[-1]

    def pop(self):
        self.check_empty_stack()
        top_value = self._stack.pop()
        if top_value == self._min_stack[-1]:
            self._min_stack.pop()  # remove min element
        return top_value
