# A simple Python program to introduce a linked list

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null

    def __str__(self):
        return f'{self.__class__.__name__}({self.data})'


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    @classmethod
    def from_str(cls, ll_str):
        ll = cls()
        ll.head = Node(ll_str[0])
        curr_node = ll.head
        for letter in ll_str[1:]:
            curr_node.next = Node(letter)
            curr_node = curr_node.next
        return ll

    def __str__(self):
        str_representation = ""
        curr_node = self.head
        while curr_node is not None:
            str_representation += '->' + str(curr_node.data)
            curr_node = curr_node.next
        return str_representation


def find_element(l_list: LinkedList, k: int):
    curr_node = l_list.head
    node_index = 0
    while curr_node is not None:
        if node_index == k:
            return curr_node
        curr_node = curr_node.next
        node_index += 1
    return None


def return_kth_last_element(l_l: LinkedList, k: int) -> Node:
    """
    Q 2.2
    """
    kth_from_start_node = find_element(l_l, k - 1)
    curr_node = l_l.head
    while kth_from_start_node.next is not None:
        curr_node = curr_node.next
        kth_from_start_node = kth_from_start_node.next
    return curr_node


def remove_dups(l_list: LinkedList) -> LinkedList:
    """
    l_list_str: str representation of single linked list
    Q 2.1
    """
    if l_list.head is None:
        return l_list

    nodes_data = set()
    prev_node = l_list.head
    current_node = l_list.head
    while current_node is not None:
        next_node = current_node.next
        if current_node.data in nodes_data:
            prev_node.next = next_node
        else:
            nodes_data.add(current_node.data)
            prev_node = current_node  # chane pre node only if node wat not deleted
        current_node = next_node
    return l_list


def test_remove_dups():
    l_l = LinkedList()
    l_l.head = Node('a')
    curr_node = l_l.head
    for letter in 'abbcca':
        curr_node.next = Node(letter)
        curr_node = curr_node.next
    print(remove_dups(l_l))


