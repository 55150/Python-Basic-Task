#Find LCM and GCM of a Number 
class LCM_GCM():
    def __init__(self,num_1,num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def lcm(self):
        if self.num_1 > self.num_2:
            greater = self.num_1
        else:
            greater = self.num_2
        while True:
            if greater%self.num_1==0 and greater%self.num_2==0:
                lcm = greater
                break
            greater+=1
                
        print(lcm)
            
    def gcm(self):
        if self.num_1 < self.num_2:
            smaller = self.num_1
        else:
            smaller = self.num_2
        for i in range(1,smaller+1):
            if self.num_1%i == 0 and self.num_2%i==0:
                gcd = i
        print(gcd)

while True:
    try:
        num_1 = int(input("Enter Number 1 :"))
        num_2 = int(input("Enter Number 2 :"))
        choice = input("select your choice into Below Option \n (1) LCM \n (2) GCM\n (3) Exit\n\n Please Enter Your Choice :")
        l1 = LCM_GCM(num_1,num_2)
        if choice == 1:
                l1.lcm()
        elif choice == 2:
            l1.gcm()
        elif choice == 3:
            print(f" LCM and GCM Find Stop ")
            break
        else:
            print(f" Error : Invalid Choice")
    except ValueError:
        print("Error : Please Enter only Integer")
        continue
