"""
Code written by Curtis Godwin -- cmg39658@uga.edu
"""

import random

#sorting algorithms
class Sorts:
    # partition function for normal quick sort
    # A is the list, r is the rightmost index, and p is the partition index
    def partition(self,A, p, r):
        x = A[r]
        i = p - 1
        for j in range (p, r):
            if A[j] <= x:
                i = i + 1
                temp_val = A[i]
                A[i] = A[j]
                A[j] = temp_val
        temp_val = A[i+1]
        A[i+1] = A[r]
        A[r] = temp_val
        return i + 1


    # wide_partition quicksorts a list with two dimensions
    # NOTE: dimension to be sorted must be the second dimension
    #       (desired elements to be sorted should be at the second index)
    # A is the list, r is the rightmost index, and p is the partition index
    def wide_partition(self, A, p, r):
        x = A[r][1]
        i = p - 1
        for j in range(p, r):
            if A[j][1] <= x:
                i = i + 1
                temp_val = A[i]
                A[i] = A[j]
                A[j] = temp_val
        temp_val = A[i+1]
        A[i+1] = A[r]
        A[r] = temp_val
        return i + 1

    # quick_sort works recursively with the partition function
    # A is the list to be sorted, p is the leftmost index, and r is the rightmost index
    # wide_bool indicates whether the list being sorted has two dimensions
    def quick_sort(self, A, p, r, wide_bool):
        #the base case of quick_sort -- stop performing the recursion when
        #there is only one element in the partition
        #in this implementation, this is checked by seeing if the leftmost
        #index is still left of the rightmost index
        if p < r:
            if wide_bool == False:
                #partition the list -- split the list into two lists
                #where the first list contains elements less than the middle value and the
                #second list contains elements greater than the middle value
                q = self.partition(A, p, r)
            else:
                q = self.wide_partition(A, p, r)
            #now that the list has been partitioned, quick sort the first half
            self.quick_sort(A, p, q-1, wide_bool)
            #now quicksort the second half
            self.quick_sort(A, q+1, r, wide_bool)

    #quicksorts a list given only that list as input
    #inputs the start and end of the list for the quick sort parameters
    def quick_sort_easy(self, A, wide):
        self.quick_sort(A,0,len(A)-1,wide)



#quick_sort = Sorts()

#example_list = [10,10,10,10,10,1099,1099,1099,4,2,9,8,3,11,5,1,6,12,13,77,1099,14,29,15]

#quick_sort.quick_sort_easy(example_list, wide=False)

#print(example_list)
