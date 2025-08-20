def insertionSort(data):
    while True:
        choice = input("select your choice into Below Option \n (1) Ascending \n (2) Descending\nPlease Enter Your Choice :")
        if not choice.isdigit():
            print(" Error : Please Enter Only Digits")
            continue
        choice = int(choice)
        
        #Ascending
        if choice == 1:
            for i in range(1,len(data)):
                current = data[i]
                previous = i-1
                while previous>=0 and data[previous]>current:
                    data[previous+1] = data[previous]
                    previous -=1
                data[previous+1] = current
            print(f"Ascending : {data}") 
            break
        #Descending
        elif choice == 2:
            for i in range(1,len(data)):
                current = data[i]
                previous = i-1
                while previous>=0 and data[previous]<current:
                    data[previous+1] = data[previous]
                    previous -=1
                data[previous+1] = current
            print(f"Descending : {data}")
            break
        else:
            print(" Error : Invalid Choice ")
print("--------Insertion Sort-------")
data = [50,20,70,40,30,10,60]
print(f" Static List : {data}")
insertionSort(data)

