class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def createLL(self,n):
        i=0
        while i<n:
            a=i+1
            if a%2 !=0:
                val=int(input("Enter data: "))
                new_node=Node(val*val)
            else:
                val=int(input("Enter data: "))
                new_node=Node(val*2)
            if self.head==None:
                self.head=new_node
            else:
                t=self.head
                while t.next != None:
                    t=t.next
                t.next=new_node
            i=i+1
    def show(self,head):
        t=head
        print("\n list of nodes: ")
        s=0
       
        while t:
            print(t.val,end=" ")
            s=s+t.val
            t=t.next
        print(" \n sum:",s)
    def split(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None
        print("First linked list :")
        self.show(self.head)
        print("Second linked list :")
        self.show(second)
obj=Linkedlist()
n=int(input("enter n value: "))
obj.createLL(n)
obj.show(obj.head)
obj.split()
