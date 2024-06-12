# # Q2. find the laregst of three number?

def calculate_large(n1, n2, n3):
    if (n1 > n2 and n1> n3):
        print(n1)

def find_largest_number(n1, n2, n3):
        calculate_large(n1, n2, n3) # n1 will be the greatest
        calculate_large(n2, n1, n3)  # n2 will be the greatest
        calculate_large(n3, n1, n2) # n3 will be the greatest

find_largest_number(10,40,311)