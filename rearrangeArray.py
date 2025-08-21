def rearrangeArray():
    # array = [2,3,8,1,4,0,5,7,6,9]
    array = [4, 0, 3, 1, 2]
    rearrange_array = [None]*len(array)
    for i in range(len(array)):
        index = array[i]
        rearrange_array[index] = i

    print(rearrange_array)
rearrangeArray()