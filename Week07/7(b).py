class QueueArray:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*size
        self.front=-1
        self.rear=-1
    def enqueue(self,data):
        if self.rear==self.size-1:
            print("Queue Overflow")
        else:
            if self.front==-1:
                self.front=0
            self.rear+=1
            self.queue[self.rear]=data
            print(f"{data} is inserted into the queue")
    def dequeue(self):
        if self.front==-1 or self.front>self.rear:
            print("Queue underflow")
        else:
            x=self.queue[self.front]
            self.queue[self.front]=None
            self.front+=1
            print(f"{x} is deleted from the queue")
            if self.front>self.rear:
                self.front=-1
                self.rear=-1
    def peek(self):
        if self.front==-1:
            print("Queue is empty")
        else:
            print(f"Peek: {self.queue[self.front]}")
    def display(self):
        if self.front==-1:
            print("Queue is empty")
        else:
            for i in range(self.front,self.rear+1):
                print(self.queue[i])
size=int(input("Enter size"))
Queue=QueueArray(size)
while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    choice=int(input("Enter your choice"))
    if choice==1:
        data=int(input("Enter a value"))
        Queue.enqueue(data)
    elif choice==2:
        Queue.dequeue()
    elif choice==3:
        Queue.peek()
    elif choice==4:
        Queue.display()
    elif choice==5:
        break
    else:
        print("Invalid choice")