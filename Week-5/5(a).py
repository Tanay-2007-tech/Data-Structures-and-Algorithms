class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SinglyLinkedList:
    def __init__(self):
        self.head=None
    def create(self):
      n=int(input("Enter the no of values"))
      for i in range(n):
            x=int(input("Enter the value"))
            new=Node(x)
            if self.head is None:
                self.head=new
            else:
                temp=self.head
                while temp.next:
                    temp=temp.next
                temp.next=new

    def display(self):
     current=self.head
     while current is not None:
        print(current.data,end="->")
        current=current.next
     print("None")
    def insert_begin(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
        else:
            temp=new
            temp.next=self.head
            self.head=temp
    def insert_end(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=new
    def insert_atindex(self,index,data):
        new = Node(data)
        if index==0:
            new.insert_begin()
        elif self.head is None:
            self.head=new
        else:
            temp = self.head
            for i in range(index-1):
                temp=temp.next
            new.next=temp.next
            temp.next=new
    def deletion_begin(self):
        if self.head is None:
            print("List is empty")
        else:
           self.head=self.head.next
    def deletion_end(self):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head
            while temp.next.next!=None:
                temp=temp.next
            temp.next=None
    def deletion_index(self,index):
        if index<0:
            print("Invalid index")
        elif self.head is None:
            print("Deletion cant be performed")
        elif index==0:
            self.deletion_begin()
        else:
            temp = self.head
            for i in range(index-1):
                temp=temp.next
            temp.next=temp.next.next
    def count(self):
        c=0
        temp=self.head
        while temp!=None:
            c+=1
            temp=temp.next
        print("The number of nodes: ",c)

L=SinglyLinkedList()
while True:
    print("1.Create")
    print("2.Insertion at begin")
    print("3.Insertion at end")
    print("4.Insertion at specific Index")
    print("5.Deletion at begin")
    print("6.Deletion at end ")
    print("7.Deletion at specific index")
    print("8.Count Number of nodes: ")
    print("9.Display")
    print("10.Exit")

    choice=int(input("Enter your Choice: "))

    if choice==1:
        L.create()
    elif choice==2:
        x = int(input("Enter value: "))
        L.insert_begin(x)
    elif choice==3:
        x = int(input("Enter value: "))
        L.insert_end(x)
    elif choice==4:
        index=int(input("Enter index"))
        x = int(input("Enter value: "))
        L.insert_atindex(index,x)
    elif choice==5:
        L.deletion_begin()
    elif choice==6:
        L.deletion_end()
    elif choice==7:
        index = int(input("Enter value: "))
        L.deletion_index(index)
    elif choice==8:
        L.count()
    elif choice==9:
        L.display()
    elif choice==10:
        break
    else:
        print("Invalid Choice")
