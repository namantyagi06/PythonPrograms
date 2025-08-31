# #1.Reverse an array using Recursion.

# def reversing(arr,left,right):
#     if left>=right:
#         return arr
#     arr[left],arr[right]=arr[right],arr[left]
#     return reversing(arr,left+1,right-1)

# arr=[1,2,3,4,5,6,7,8]
# print(reversing(arr,0,len(arr)-1))


# #2.check if the string is pallindrome or not

# def checkpallindrome(s,left,right):
#     if left>=right:
#         return True
#     if s[left]!=s[right]:
#         return False
#     return checkpallindrome(s,left+1,right-1)

# s="naman"
# print(checkpallindrome(s,0,len(s)-1))
    

# #3.find the fibonacci number
# def fib(n):
#     if n==0 or n==1:
#         return n
#     return fib(n-1)+fib(n-2)

# print(fib(5))
# print(fib(10))

#4.