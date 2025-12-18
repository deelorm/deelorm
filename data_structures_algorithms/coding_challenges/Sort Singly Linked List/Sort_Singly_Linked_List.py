
#Task --- Create a singly linked list structure and define a sort function that can sort linked list in ascending order


#Singly Linked List Node
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

#Singly Linked List class, with sort function
class Ldlist:
    def __init__(self, head=None):
        self.head = head

#Prints elements in linkedlist
    def printList(self):
        link = self.head
        while link != None:
            print(link.data, end=" ")
            link = link.next
        print("")

 #Inserts node at the beginning of the linkedlist
    def insertBegin(self, node):
        link = self.head
        if link == None:
            self.head = node
        else:
            node.next = link
            self.head = node

#Sorts linkedlist in ascending order
    def sortList(self):
        link = self.head
        while link.next != None:
            link2 = link.next
            swp = 0
            while link2 != None:
#                var = None
                if link.data > link2.data:
                    if link == self.head:
                        var = link
                        self.head = link2
                        var.next = link2.next
                        link2.next = var
                        swp = 1
                    elif link2.next == None:
                        var = link2
                        link.next = None
                        var.next = prev.next
                        prev.next = var
                        swp = 1
                    else:
                        var = link2
                        link.next = link2.next
                        var.next = prev.next
                        prev.next = var
                        swp = 1
                prev = link
                link = link2
                link2 = link2.next
            if swp == 0:
                break
            link = self.head


##############################################################################################################
############## Main Code block ###############################################################################

a1  = Node(10)
l1 = Ldlist(a1)
a2 = Node(30)
a3 = Node(35)
a4 = Node(25)
a5 = Node(35)

l1.insertBegin(a2)
l1.insertBegin(a3)
l1.insertBegin(a4)
l1.insertBegin(a5)
l1.sortList()
l1.printList()
