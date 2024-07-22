
n = int(input("Enter number: "))
print("\n")
i , j = 0,1
print(i )
print(j)
for x in range(0,n):
	s = i + j
	i = j 
	j = s
	print(s)	
 
# input: 5
# Output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8