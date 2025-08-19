class CircularQueue:
    def __init__(self,capacity):
        self.capacity = capacity
        self.front = -1
        self.rear = -1
        self.Circular_queue =[None]*capacity

    def enqueue(self):
        if (self.rear + 1) % self.capacity == self.front:
            print(" Error: Circular Queue is full")
            return
            
        data_element = input("Enter EnQueue :")
        if not data_element.strip():
            print(' Error : Please Enter Number Or String')
            return
        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            #increment rear 
            self.rear = (self.rear+1)%self.capacity

        self.Circular_queue[self.rear] =data_element
        
        print(f" {data_element} Enqueue in Circular Queue")

    def dequeue(self):
        if self.front == -1:
            print("Error: Circular Queue is Empty")
            return
        print(f"{self.Circular_queue[self.front]} DeQueue in  Circular Queue ")
        self.Circular_queue[self.front] = None
        print(self.Circular_queue)
        if self.front == self.rear:   # only one element
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

    def frontPeek(self):
        if self.front != -1:
            print(f"Front : {self.Circular_queue[self.front]}")
        else:
            print("Error: Circular Queue is Empty")

    def rearPeek(self):
        if self.rear != -1:
            print(f"Queue Tail :{self.Circular_queue[self.rear]} ")
        else:
            print("Error :Circular Queue Is Empty")

    def exits(self):
        print(' Circular Queue Process End')
        exit()
    
    def showQueue(self):
        if self.front == -1:
            print("Error : Circular Queue is Empty")
        else:
            print(f"Queue : {self.Circular_queue}")

    def choice(self):
        while True:
            choice = input("select your choice into Below Option \n (1) EnQueue \n (2) DeQueue\n (3) Front\n (4) Rear\n (5) Exit\n (6) Display Your Circular Queue\n\n Please Enter Your Choice :")
         
            if not choice.isdigit():
                print(" Error : Please Enter Only Digits")
                continue
            choice = int(choice)
    
            if choice == 1:
                self.enqueue()

            elif choice == 2:
                self.dequeue()

            elif choice == 3:
                self.frontPeek()

            elif choice == 4:
                self.rearPeek()

            elif choice == 5:
                self.exits()

            elif choice == 6:
                self.showQueue()

            else:
                print(f" Error : Invalid Choice")

while True:
        capacity = input("Enter Your Circular Queue capacity :")
        if not capacity.isdigit():
            print('Please Enter Digit Only')
            continue
        else:
            capacity = int(capacity)
            c1 = CircularQueue(capacity)
            c1.choice()
            break
