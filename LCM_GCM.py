#Find LCM and GCM of a Number 
#Function Based
def lcm_gcm(num_1,num_2):
    #gcm
    if num_1 < num_2:
        smaller = num_1
    else:
        smaller = num_2
    for i in range(1,smaller+1):
        if num_1%i == 0 and num_2%i==0:
            gcd = i
    print(gcd)
    #lcm
    if num_1 > num_2:
        greater = num_1
    else:
        greater = num_2
    while True:
        if greater%num_1==0 and greater%num_2==0:
            lcm = greater
            break
        greater+=1
            
    print(lcm)

while True:
    try:
        num_1 = int(input("Enter Number 1 :"))
        num_2 = int(input("Enter Number 2 :"))
        lcm_gcm(num_1,num_2)
        break
    except ValueError:
        print("Error : Please Enter only Integer")
        continue
