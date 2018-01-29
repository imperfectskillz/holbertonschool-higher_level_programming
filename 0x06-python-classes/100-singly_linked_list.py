#!/usr/bin/python3
"""
Module containing class Node
"""


class Node:
    """
    Class Node singly linked
    """

    def __init__(self, data, next_node=None):
        """
        initlizing attr
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        returns data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        sets data value
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        returns next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        sets node_next as value
        """
        if value is not None or not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    """
    class SinglyLinkedList
    """
    def __init__(self):
        """
        contains private head with no getter setter
        """
        self.__head = None

    def __str__(self):
        """
        returns str rep
        """
        if self.__head is None:
            return

        current = self.__head
        result = ""
        while current is not None:
            result += str(current.data)
            if current.next_node is not None:
                result += "\n"
            current = current.next_node
        return result

    def sorted_insert(self, value):
        """
        inserts new Node
        """
        if self.__head is None:
            self.__head = Node(value, self.__head)
            return
        if value < self.__head.data:
            self.__head = Node(value, self.__head)
            return
        current = self.__head
        while value > current.next_node.data:
            current = current.next_node
        current.next_node = Node(value, current.next_node)
