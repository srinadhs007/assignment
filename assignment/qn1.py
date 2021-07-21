import sys
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
# method to add new node at the beginning
    def addNode(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
# method to delete a node taking position of node as a parameter
    def deleteatpos(self, pos):
        if self.head == None:
            return
        temp = self.head

        if pos == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(pos -1 ):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return
        if temp.next is None:
            return

        next = temp.next.next
        temp.next = None
        temp.next = next
#method to print linked list
    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data,end=" ")
            temp = temp.next
        print("")
#method to delete all the nodes with a given value
    def deleteAll(self,val):
        if(self.head.data == val):
            self.head = self.head.next
        temp = self.head
        while(temp and temp.next):
            if(temp.next.data == val):
                temp.next = temp.next.next
            temp = temp.next
# method to get memory occupied by the linked list
    def getmemory(self):
        temp =  self.head
        count =0
        while(temp):
            count+=1
            temp = temp.next
        return count*(sys.getsizeof(self.head))
#method to delete all nodes with given value and next subsequent node
    def deleteAllandNext(self,val):
        while(self.head.data == val):
            self.head = self.head.next
            if(self.head.data == val):
                self.head = self.head.next
                self.head = self.head.next
            else:
                self.head = self.head.next
        temp = self.head
        while(temp and temp.next and temp.next.next):
            if(temp.next.data == val):
                k = temp.next
                temp.next = k.next.next
                k.next = None
            if(temp.next):
                if(temp.next.next):temp = temp.next
            else:break
        if(temp.next and temp.next.data == val):
            temp.next = None
#driver code to check the above methods
llist = LinkedList()
llist.addNode(7)
llist.addNode(1)
llist.addNode(3)
llist.addNode(6)
llist.addNode(2)
llist.addNode(8)
llist.addNode(1)
print("\nOriginal Linked List:")
llist.printList()
llist.deleteatpos(3)
print("\nLinked list after deleting a node at position 3:")
llist.printList()
llist.deleteAll(1)
print("\nLinked List after deleting Node with value 1:")
llist.printList()
llist.deleteAllandNext(2)
print("\nLinked List after deleting node with value 2 and next Node:")
llist.printList()
print("\nMemory occupied by Linkedlist:")
print(llist.getmemory())