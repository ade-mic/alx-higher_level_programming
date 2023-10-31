#!/usr/bin/python3
"""
This module defines a Node class.

The Node class defines a node of singly linked list.
"""


class Node:
    """
    A node of singly liked list

    Attributes:
        data(int):  an integer Type otherwise raise a TypeError
        next_node(): can be None or must be a Node.

    Methods:
        __init__(data, next_node=None): The constructor for Node class.
    """
    def __init__(self, data, next_node=None):
        """The constructor for Node class"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Retrieve value of data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the value of data"""
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """Retrieve value of next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the value of next_node"""
        if isinstance(value, None) or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """
    A node of singly liked list

    Attributes:
        head:  head node

    Methods:
        __init__(data, next_node=None): The constructor for Node class.
        sorted_inserted(value)
    """
    def __init__(self):
        """Constructor of SiglyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """insert a new node into the correct sorted position in the list
        increaasing order
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node and value > current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Return a strinf representation of the linked list

        Returns:
            str: A string containing one node number per line.
        """
        result = ""
        current = self.__head
        while current:
            result += str(current.data) + '\n'
            current = current.next_node
        return result
