'''
Insertion algorithm.
1. First element is considered as sorted and a subset to compare with the rest of the elements.
2. The nth element  is compared with n-1 element  and if  nth element is greater than the  n-1 element then n-1 element is assigned the value of n.
3. We now find a position for the nth element in the sorted subset by moving left and when we find it, we insert this nth element.
'''
def insertion_sort(arr):
    for x in range(len(arr)):
        current_value = arr[x]                
        position =x
        while position  > 0 and arr[x -1] > current_value: # Skips the 0th  position as it is considered as sorted and goes to the 1st positon 
           arr[x] = arr[x-1]                               #Checks if the sorted element is greater than the current value,
           position -= 1                                   #if yes, then the sorted element is assigned the current position 
                                                           #The while loop continues until it finds a position for the current value [arr[x -1] > current_value,position -= 1]
                                                           #Once it finds the correct position we assign the current value [arr[position]  = current_value]
            
            
        arr[position]  = current_value
    return arr



if __name__ == '__main__':
    arr = [5, 4, 3, 2, 1, 7, 8, 9, 9, 7, 1]
    print(insertion_sort(arr))
