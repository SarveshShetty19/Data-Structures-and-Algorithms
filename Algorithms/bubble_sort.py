'''
In Bubble sort , we sort the the current element with the adjacent element.
If the value of the current element is less than the adjacent element than we swap it.
Eg:
[5,4,3,2,1,7,8,9]

In the first iteration [Inner Loop in the code],The current element 5 is compared with 4 as 5 is greather than 4 ,Swap takes place.
In next step, 5 is compred to 3 and swap takes place and so on until we have the largest element to the right hand side.
[5,4,3,2,1,7] -> Swap 4 with 5
[4,5,3,2,1,7] -> Swap 3 with 5
[4,3,5,2,1,7] -> Swap 2 with 5
[4,3,2,5,1,7] -> Swap 1 with 5
[4,3,2,1,5,7]-> No Swap
'''
def bubble_sort(arr):
    for _ in range(len(arr) - 1): # Outer for loop to make the loop underlying loop run n-1 times from 0th element.
        for i in range(len(arr) - 1): #Inner loop to compare current element with next element.
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]  #Swap the numbers

    return numbers

if __name__ == '__main__':
    arr=[5,4,3,2,1,7,8,9]
    print(bubble_sort(arr))
