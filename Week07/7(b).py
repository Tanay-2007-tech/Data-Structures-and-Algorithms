
class Node:
    def __init__(self ,data):
        self.dat a =data
        self.nex t =None
class Queue:
    def __init__(self):
        self.fron t =None
        self.rea r =None
        self.siz e =0
    def enqueue(self ,item):
        new_nod e =Node(item)
        if self.rear is None:
            self.fron t =new_node
            self.rea r =new_node
        else:
            self.rear.nex t =new_node
            self.rea r =new_node

    def dequeue(self):
        if self.front and self.rear is None:
            print("Queue Underflow")
        else:
            if self.fron t= =self.rear:
                self.fron t =None
                self.rea r =None
            else:
                self.fron t =self.front.next
            if self.front is None:
                self.rea r =None
    def peek(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            print(f"Peek:{self.front.data}")
    def display(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            while self.front is not None:
                print(self.front.data)
                self.fron t =self.front.next

q 1 =Queue()
while True:
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Peek")
    print("4.Display")
    print("5.Exit")

    choic e =int(input("Enter Your Choice"))

    if choic e= =1:
        ite m =int(input("Enter value"))
        q1.enqueue(item)
    elif choic e= =2:
        q1.dequeue()
    elif choic e= =3:
        q1.peek()
    elif choic e= =4:
        q1.display()
    else:
        break



