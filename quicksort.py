"""
Python simple implementation of quicksort with last position pivot

This is the lomuto scheme which can be optimized by a smarter
pivot selection method.

Author:  Christopher Gleeson, 2015
Copyright 2016 Christopher Gleeson. All rights reserved.
"""

def _partition(numbers, start, end):
    """
    _partition(numbers, start, end)
    Inputs:  A list of numbers, the start and end index for that list
    Outputs:  The pivot index is returned, the list is reordered in place.
    """
    #classic pivot at end implementation
    pivot = numbers[end]
    i = start
    j = start
    while j <= (end-1):
        if numbers[j] <= pivot:
            #swap n[i] and n[j] and increment i
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp
            i += 1
        j += 1
    #At the end, n[i] will hold a value larger than pivot
    temp = numbers[i]
    numbers[i] = pivot
    numbers[end] = temp
    return i

def quicksort(numbers, start, end):
    """
    quicksort(numbers, start, end)
    Inputs:  A list of numbers, the start and end index for that list
    Outputs:  The list is sorted in place.
    """
    if start < end:
        pivot = _partition(numbers, start, end)
        quicksort(numbers,start,pivot-1)
        quicksort(numbers,pivot+1,end)
    return numbers

#Testing section
myNumbers = [3,6,7,4,2,1,5,15,15,25,-1,-8,0]
print "Quicksort of ",
print myNumbers
quicksort(myNumbers,0,len(myNumbers)-1)
print "Sorted list is: ",
print myNumbers
