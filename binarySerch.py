def binarySerch(data,Target):
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
    print(f"Ascending : {data}")
    start = 0
    end = len(data)-1
    while start <= end:
        mid = (start+end)/2
        if Target > data[mid]:
            start = mid+1
        elif Target < data[mid]:
            end = mid-1
        elif Target == data[mid]:
            print(f" Your Target Value Index is {mid}")
        else:
            print(f" This list does not contain your target. So Return {-1}")

            
                 
print("--------Bubble Sort-------")
data = [50,20,70,40,30,10,60]
print(f" Static List : {data}")
while True:
    Target = input("Enter Your Circular Queue capacity :")
    if not Target.isdigit():
        print('Please Enter Digit Only')
        continue
    else:
        Target = int(Target)
        break
binarySerch(data,Target)

