# print my name n times using recursion, l.n. 5
# print liner number 1 to N
# print liner number N to 1
# print sum of N number.
# WAP to print factorial of a Number.
# WAP to reverse a array.
# WAP to return True if the given string is palindrome.
# WAP to find the fibonacci number
#  find maximum from the array

class Recursion:

    def print_name(self, name, n):
        i = 0
        return self.name(name, n, i)
    
    def name(self, name, n, i):
        if i == n:
            return
        print(name)
        self.name(name, n, i+1)

    def print_numbers(self, nums, i=1):
        if i > nums:
            return
        print(i)
        self.print_numbers(nums,i+1)

    def print_number_to_zero(self, nums):
        if nums == 0:
            return
        print(nums)
        self.print_number_to_zero(nums-1)

    def print_sum_number(self, num, sum=0):
        if num == 0:
            print(sum)
            return None
        sum += num
        self.print_sum_number(num-1, sum)
        
    def factorial_number(self, num):
        if num == 0:
            return 1
        return num * self.factorial_number(num-1)

    def reverse_array(self, arr, i = 0):
        n = len(arr)
        if i >= n//2:
            print(arr)
            return
        arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
        self.reverse_array(arr, i+1)
        
    def check_palindrome(self, s, i=0):
        len_str = len(s)
        if (i >= len_str//2):
            print(True)
            return True
        if (s[i] != s[len_str-i-1]):
            return False
        self.check_palindrome(s, i+1)

    def fibonacci(self, num):
        if (num <= 1):
            return num

        return self.fibonacci(num-1) + self.fibonacci(num-2)

    def find_max(self, arr, i=0, m=0):
        len_arr = len(arr) - 1
        if i >len_arr:
            print(m)
            return
        if arr[i] > m:
            m = arr[i]
        self.find_max(arr, i+1, m)


r = Recursion()

# r.print_name("Harshit", 4)
# r.print_numbers(4)
# r.print_number_to_zero(4)
# r.print_sum_number(4)
# print(r.factorial_number(2))
# print(r.reverse_array([1,2,3,5]))
# print(r.check_palindrome("MOMO"))
# print(r.fibonacci(6))
# print(r.find_max([11,2,32,4,5,8]))

