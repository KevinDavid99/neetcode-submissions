"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_nodes = {}
        current = head
        while current:
            new_nodes[current] = Node(current.val)
            current = current.next
        current = head
        while current:
            new_nodes[current].next = new_nodes.get(current.next)
            new_nodes[current].random = new_nodes.get(current.random)
            current = current.next
        return new_nodes.get(head)