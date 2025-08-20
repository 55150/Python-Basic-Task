def bubbleSort(data):
    while True:
        choice = input("select your choice into Below Option \n (1) Ascending \n (2) Descending\nPlease Enter Your Choice :")
        if not choice.isdigit():
            print(" Error : Please Enter Only Digits")
            continue
        choice = int(choice)
        
        #Ascending
        if choice == 1:
            for i in range(len(data)-1):
                for j in range(len(data)-i-1):
                    if data[j] > data[j+1]:
                        data[j],data[j+1] = data[j+1],data[j]
            print(f"Ascending : {data}")
            break
        #Descending
        elif choice == 2:
            for i in range(len(data)-1):
                for j in range(len(data)-i-1):
                    if data[j] < data[j+1]:
                        data[j],data[j+1] = data[j+1],data[j]
            print(f"Descending : {data}")
            break
        else:
            print(" Error : Invalid Choice ")
            
                 
print("--------Bubble Sort-------")
data = [50,20,70,40,30,10,60]
print(f" Static List : {data}")
bubbleSort(data)

