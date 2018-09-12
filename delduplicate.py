#
class Node:

    def __init__(Node, data):
        Node.data = data  # Assign data
        Node.next = None  # Initialize next as null

def traverse(head):
        current = head  # start from the head node
        while current != None:
            print(current.data)  # access the node value
            current = current.next  # move on to the next node

def deleteDuplicates(head):
    if(head==None or head.next==None):
        return head

    prev=head
    nextnode=head.next

    while(nextnode!=None):
        if(nextnode.data==prev.data):
            prev.next=nextnode.next
            nextnode=nextnode.next

        else:
            prev=nextnode
            nextnode=nextnode.next

    return head

head = Node(10)
nodeB = Node(10)
nodeC = Node(20)
nodeD = Node(30)
nodeE = Node(30)
nodeF = Node(40)

head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF

head=deleteDuplicates(head)
traverse(head)