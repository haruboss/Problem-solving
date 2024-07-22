i = int(input("Enter number:"))
sum = 0
while (i>0 or sum>9):
    if i == 0:
        i = sum
        sum = 0
    sum = sum + i % 10
    i = i // 10
print(sum)


# Input: 43
# Output: 7