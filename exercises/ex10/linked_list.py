"""Utility functions for working with Linked Lists."""
 
from __future__ import annotations
 
__author__ = "730659778"
 
 
class Node:
    """An item in a singly-linked list."""
    data: int
    next: Node | None
 
    def __init__(self, data: int, next: Node | None):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next
 
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:
        """Returns the first value."""
        return int(self.data)
    
    def tail(self) -> Node | None:
        """Returns a new Node minus the head."""
        if self.next is None:
            return None
        else:
            return Node(self.next.data, self.next.next)
    
    def last(self) -> int:
        """Returns the data of the last node."""
        idx = self
        while idx.next is not None:
            idx = idx.next
        return idx.data


def value_at(head: Node | None, index: int) -> int:
    """Recursively finds the value at the index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:
        return head.data
    else:
        return value_at(head.next, index - 1)
    

def max(head: Node | None) -> int:
    """Recursively finds the val;
    ue of the maximum in the list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is None:
        return head.data
    elif head.next.data > head.data:
        return max(head.next)
    else:
        return head.data


def linkify(input_list: list[int]) -> Node | None:
    """Makes a normal list a Node list."""
    if len(input_list) == 0:
        return None
    else:
        new_node: Node = Node(input_list[0], linkify(input_list[1:]))
        return new_node


def scale(head: Node | None, factor: int) -> Node | None:
    """Scales up by the factor."""
    if head is None:
        return None
    else:
        head.data *= factor
        head.next = scale(head.next, factor)
        return head