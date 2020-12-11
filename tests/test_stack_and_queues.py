import pytest
from stack_and_queues import EmptyStack, StackMin


def stack_min_from_array(arr):
    min_stack = StackMin()
    for item in arr:
        min_stack.push(item)
    return min_stack


@pytest.mark.parametrize('min_stack, min_value', [
    (stack_min_from_array([7, 5, 1, 10, 50, 3]), 1),
    (stack_min_from_array([-50, 5, 1, 10, 50, 3]), -50),
    (stack_min_from_array([-50, 5, 1, 10, 50, -80]), -80),
    (stack_min_from_array([7, 5, 1, -4, 50, 3]), -4),

])
def test_min_value(min_stack, min_value):
    assert min_stack.min() == min_value


def test_empty_stack_exception():
    with pytest.raises(EmptyStack):
        min_stack = stack_min_from_array([1])
        assert min_stack.pop() == 1
        min_stack.peek()
