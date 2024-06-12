# print my name n times using recursion, l.n. 5
# print liner number 1 to N
# print liner number N to 1
# print sum of N number.
# WAP to print factorial of a Number.
# WAP to reverse a array.
# WAP to return True if the given string is palindrome.
# WAP to find the fibonacci number


class Recursion:
    
    def print_my_name(self, name, n_times, i=0):
        if (i == n_times):
            return
        print(name)
        self.print_my_name(name, n_times, i+1)

    def print_one_to_N(self, N, index=1):
        if (index > N): return
        print(index)
        self.print_one_to_N(N, index+1)
    
    def print_N_to_one(self, number):
        if (number == 0): return
        print(number)
        self.print_N_to_one(number-1)

    def sum_of_number(self, num, sum=0):

        # using a parameterised recursion 
        # if (num == 0):
        #     print(sum)
        #     return None
        # self.sum_of_number(num-1, sum+num)

        # we can solve it by functional recursion

        if (num == 0):
            return 0
        return num + self.sum_of_number(num-1)
    
    def factorial(self, N):
        if (N ==0):
            return 1
        return N * self.factorial(N-1)
        
    def reverse(self, arr, i=0):
        n = len(arr)
        if (i >= n//2):
            print(arr)
            return None
        arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
        self.reverse(arr, i+1)
        
    def is_palindrome(self, s, i=0):
        n = len(s)
        if i >= n//2:
            print(True)
            return True
        if s[i] != s[n-i-1]:
            return False
        self.is_palindrome(s, i+1)
    count = 0
    def is_fibonacci(self, n):
        self.count += 1
        if (n <= 1):
            print("count", self.count)
            return n
        return self.is_fibonacci(n-1) + self.is_fibonacci(n-2)

recursion = Recursion()

# recursion.print_my_name("Harshit", 5)
# recursion.print_one_to_N(10)
# recursion.print_N_to_one(10)
# recursion.sum_of_number(5) # print(recursion.sum_of_number(2))
# print(recursion.factorial(9))
# print(recursion.reverse([1,2,3,5]))
# print(recursion.is_palindrome("MOM"))
print(recursion.is_fibonacci(3))