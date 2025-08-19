class Queue():
    def __init__(self):
        self.queue = []
        self.tail = -1
        self.head = 0
        
    def enqueue(self):
        data_element = input("Enter EnQueue :")
        if not data_element.strip():
            print(' Error : Please Enter Number Or String')
            return
        self.tail +=1
        self.queue += [data_element]
        print(f" {data_element} Enqueue in Queue")

    def dequeue(self):
        if self.tail != -1:
            self.tail -= 1
            print(f"{self.queue[self.head]} DeQueue in Queue ")
            del self.queue[self.head]
        else:
            print(f"Error : Your Queue Is Empty")

    def headPeek(self):
        if self.tail != -1:
            print(f"Queue Head :{self.queue[0]} ")
        else:
            print("Error : Queue Is Empty")

    def tailPeek(self):
        if self.tail != -1:
            print(f"Queue Tail :{self.queue[self.tail]} ")
        else:
            print("Error : Queue Is Empty")

    def exits(self):
        print('Queue Process End')
        exit()

    def showQueue(self):
        if self.tail != -1:
            print(f" Queue :\n {self.queue}")
        else:
            print("Error : Queue Is Empty")

    def choice(self):
        while True:
            choice = input("select your choice into Below Option \n (1) EnQueue \n (2) DeQueue\n (3) Head/Front\n (4) Rear/Tail\n (5) Exit\n (6) Display Your Queue\n\n Please Enter Your Choice :")
         
            if not choice.isdigit():
                print(" Error : Please Enter Only Digits")
                continue
            choice = int(choice)
            
            if choice == 1:
                self.enqueue()

            elif choice == 2:
                self.dequeue()

            elif choice == 3:
                self.headPeek()

            elif choice == 4:
                self.tailPeek()

            elif choice == 5:
                self.exits()

            elif choice == 6:
                self.showQueue()

            else:
                print(f" Error : Invalid Choice")

q1 = Queue()
q1.choice()
