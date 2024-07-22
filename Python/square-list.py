def sq_list(n):
    nums = list(range(1,n))
    for num in nums:
        print("Square of ", num," is: ", num * num)
        

n = int(input("Enter Number: "))        
sq_list(n)