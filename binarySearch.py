def binarySerch(data,Target):
    #Bubble Sort
    while True:
        choice = input("select your choice into Below Option \n (1) Ascending \n (2) Descending\nPlease Enter Your Choice :")
        if not choice.isdigit():
            print(" Error : Please Enter Only Digits")
            continue
        choice = int(choice)
        start = 0
        index = -1
        end = len(data)-1
        #Ascending
        if choice == 1:
            for i in range(len(data)-1):
                for j in range(len(data)-i-1):
                    if data[j] > data[j+1]:
                        data[j],data[j+1] = data[j+1],data[j]
            
            while start <= end:
                mid = int((start+end)/2)
                if Target > data[mid]:
                    start = mid+1
                elif Target < data[mid]:
                    end = mid-1
                else:
                    index = mid
                    break
            break
        #Descending
        elif choice == 2:
            for i in range(len(data)-1):
                for j in range(len(data)-i-1):
                    if data[j] < data[j+1]:
                        data[j],data[j+1] = data[j+1],data[j]
            while start <= end:
                mid = int((start+end)/2)
                if Target > data[mid]:
                    end = mid-1
                elif Target < data[mid]:
                    start = mid+1
                else:
                    index = mid
                    break
            
            break
        else:
            print(" Error : Invalid Choice ")
    if index == -1:
        print(f"Your Target Not Found -1  ")
    else:
        print(f" Your Target Value {Target} Index is {index}")

print("--------Binary Search-------")
data = [50,20,70,40,30,10,60,80]
while True:
    Target = input("Enter Your Find Element :")
    if not Target.isdigit():
        print('Please Enter Digit Only')
        continue
    else:
        Target = int(Target)
        break
binarySerch(data,Target)

