import pytest
from linked_lists import (LinkedList,
                          Node,
                          find_element,
                          return_kth_last_element

                          )


@pytest.mark.parametrize('ll, n, expected_value', [
    (LinkedList.from_str('abcde'), 1, 'b'),
    (LinkedList.from_str('abcde'), 2, 'c'),
    (LinkedList.from_str('abcde'), 4, 'e'),
])
def test_find_nth_element(ll, n, expected_value):
    assert find_element(ll, n).data == expected_value


@pytest.mark.parametrize('ll, k, expected_value', [
    (LinkedList.from_str('abcde'), 1, 'e'),
    (LinkedList.from_str('abcde'), 2, 'd'),
    (LinkedList.from_str('abcde'), 5, 'a'),
])
def test_return_kth_last_element(ll, k, expected_value):
    assert return_kth_last_element(ll, k).data == expected_value


