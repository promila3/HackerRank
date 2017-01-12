"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    if head == None :
        return 0
    slow = head
    fast = head.next
    while (slow != fast):
        if (fast == None or fast.next == None) :
            return 0
        slow = slow.next
        fast = fast.next.next
        
    return 1
