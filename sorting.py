<<<<<<< HEAD
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


#3.Bubble  sorting for ascending:

def bubblesort(nums):
    n=len(nums)
    flag=True
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                flag=False
        if flag==True:
            break

    return nums        
        
nums=[4,6,3,6,8,9,2,3,1]  
print(bubblesort(nums))  
    
#2.Bubblesorting for descending:

def bubblesort(nums):
    n=len(nums)
    flag=True
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if nums[j]<nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                flag=False
        if flag==True:
            break

    return nums        
        
nums=[4,6,3,6,8,9,2,3,1]  
print(bubblesort(nums))  

#3.
=======
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
>>>>>>> 45d1a8f1206a7d905c9d7dd8fdd717f467ff784e
