#Starting node of loop detected
class Node:
    def __init__(Node,data):
        Node.data=data
        Node.next=None

def find_start_node(head):
    loopExist=0
    fast=head
    slow=head
    while(fast!=None and slow!=None and fast.next!=None):
        fast=fast.next.next
        slow=slow.next
        if (fast==slow):
            loopExist = 1
            break
    if(loopExist):
        slow=head
        while(slow!=fast):
            slow=slow.next
            fast=fast.next
        return slow
    return None

