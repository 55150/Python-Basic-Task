class Stack():
    def __init__(self,capacity):
        self.capacity = capacity
        self.top = -1
        self.stack =[]

    def push(self):
        if len(self.stack) < self.capacity:
            data_element = input("Enter stack Push Data Element :")
            if not data_element.strip():
                print("Error : Please Enter Data Element")
                return
            self.top += 1
            self.stack += [data_element]
            print(f" {data_element} Push To Stack")

        else:
            print(" Error : Stack Is Full")
            
    def pop(self):
        if len(self.stack) != 0:
            print(f"{self.stack[self.top]} pop in stack")
            del self.stack[self.top]
            self.top -= 1
        else:
            print(" Error : Stack is Empty")

    def peek(self):
        if len(self.stack) != 0:
            print(f" Stack Top :\n {self.stack[self.top]}")
        else:
            print(" Error : Stack is Empty")

    def exits(self):
        print('Stack Process End')
        exit()

    def showQueue(self):
        if len(self.stack) != 0:
            print(f" Stack :\n {self.stack}")
        else:
            print("Error : Stack Is Empty")

    def choice(self):
        while True:
            choice = input("select your choice into Below Option \n (1) Push \n (2) Pop\n (3) Peek\n (4) Exit\n (5) Display Your Stack\n\n Please Enter Your Choice :")
         
            if not choice.isdigit():
                print(" Error : Please Enter Only Digits")
                continue
            choice = int(choice)
            
            if choice == 1:
                self.push()

            elif choice == 2:
                self.pop()

            elif choice == 3:
                self.peek()

            elif choice == 4:
                self.exits()

            elif choice == 5:
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
        c1 = Stack(capacity)
        c1.choice()
        break