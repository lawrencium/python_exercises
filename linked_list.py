import unittest


class LinkedListNode(object):
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node


class LinkedList(object):
    def __init__(self):
        """
        instantiate an empty linked list
        """
        raise Exception('Implement me!')

    def insert(self, value):
        """
        inserts `value` to the end of the list
        :param value: a value to insert
        :return: None
        """
        raise Exception('Implement me!')

    def pop(self):
        """
        returns the value at the head of the list and removes it from the linked list
        :return: the value at the head of the list
        """
        raise Exception('Implement me!')

    def contains(self, value):
        """
        returns if `value` is in the linked list
        :param value: a value to search for
        :return: boolean
        """
        raise Exception('Implement me!')


class LinkedListTest(unittest.TestCase):
    def test_ContainsOnEmptyLinkedListReturnsFalse(self):
        linkedList = LinkedList()
        assert linkedList.contains(5) == False

    def test_ContainsOnInsertedValueReturnsTrue(self):
        linkedList = LinkedList()
        linkedList.insert(5)
        assert linkedList.contains(5) == True
