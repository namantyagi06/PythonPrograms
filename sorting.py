#1.Selection sort in descending order
def selectsort(nums):
    n=len(nums)
    for i in range(0,n):
        max_ind=i
        for j in range(i+1,n):
            if nums[j]>nums[max_ind]:
                max_ind=j
        nums[i],nums[max_ind]=nums[max_ind],nums[i] 
    return nums    

#2.selection sorting in ascending order

def selectsort(nums):
    n=len(nums)
    for i in range(0,n):
        min_ind=i
        for j in range(i+1,n):
            if nums[j]<nums[min_ind]:
                min_ind=j
        nums[i],nums[min_ind]=nums[min_ind],nums[i] 
    return nums    


nums=[9,6,5,4,3,2,7]   
print(selectsort(nums))


#3.insertion sorting
