'''
In selection sort, we traverse through the whole list and find the minimum element.
We then take this minimum element and swap it with the starting element of the array i.e arr[0].
After we place it to the start of the array , we change increment the starting position of the array by 1 and start traversing again to find the mimimum element.
The same algorithm can also be done in a different way by using the maximum element.
'''

def selection_sort(arr):
    for y in range(len(arr) - 1): #An Outer loop to perform the inner loops steps len(arr) - 1 times.
        mininum_number = y               #Minimum number is set to the index of 1st element of the array
        for x in range(y,len(arr)):      # We change the starting position of the array as we have already found the minimum element and placed it to the start of the array.
            if arr[x] < arr[mininum_number]:
                mininum_number = x
        arr[y], arr[mininum_number] = arr[mininum_number], arr[y]    # Swap the positions
    return arr


if __name__ == '__main__':
    arr = [5, 4, 3, 2, 1, 7, 8, 9, 9, 7, 1]
    print(selection_sort(arr))
