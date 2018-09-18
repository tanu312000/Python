#Detect Loop
class Node:
    def __init__(Node,data):
        Node.data=data
        Node.next=None

def detect_loop(head):
    fast=head
    slow=head
    while(fast!=None and slow!=None and fast.next!=None):
        fast=fast.next.next
        slow=slow.next
        if (fast==slow):
            return 1
    return 0



