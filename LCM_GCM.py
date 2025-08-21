#Find LCM and GCM of a Number 
def lcm(num_1,num_2):
    if num_1 > num_2:
        greater = num_1
    else:
        greater = num_2
    while True:
        if greater%num_1==0 and greater%num_2==0:
            lcm = greater
            break
        greater+=1
    return lcm
def gcm(num_1,num_2):
    if num_1 < num_2:
        smaller = num_1
    else:
        smaller = num_2
    for i in range(1,smaller+1):
        if num_1%i == 0 and num_2%i==0:
            gcd = i
    return gcd
while True:
    try:
        choice = int(input("select your choice into Below Option \n (1) LCM \n (2) GCM\n (3) Exit\n Please Enter Your Choice :"))
        if choice == 1:
            num_1 = int(input("Enter Number 1 :"))
            num_2 = int(input("Enter Number 2 :"))    
            print(f"{num_1} and {num_2} LCM is {lcm(num_1, num_2)}")
        elif choice == 2:
            num_1 = int(input("Enter Number 1 :"))
            num_2 = int(input("Enter Number 2 :"))
            print(f"{num_1} and {num_2} GCD is {gcm(num_1, num_2)}")
        elif choice == 3:
            print(f" LCM and GCM Find Stop ")
            break
        else:
            print(f" Error : Invalid Choice")
    except ValueError:
        print("Error : Please Enter only Integer")
        continue
