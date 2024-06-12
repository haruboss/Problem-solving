# https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/


class Patterns:
    def one(self, n):
        for _ in range(n):
            print("*"*n)
        
    def two(self, n):
        for i in range(n):
            print("*"*(i+1))
                    
    def three(self, n):
        for i in range(1, n+1):
            for j in range(i):
                print(j+1, end="")
            print("")

    def four(self, n):
        for i in range(1, n+1):
            for j in range(i):
                print(i, end="")
            print("")

    def five(self, n):
        for i in range(n, 0, -1):
            print("*"*(i))

    def six(self, n):
        for i in range(n,0, -1):
            for j in range(i):
                print(j+1, end="")
            print("")

    def seven(self, n):
        for i in range(n):
            print(" "*(n-i-1) + ("*"*(2*i+1)) + (" "*(n-i+1)))

    def eight(self, n):
        for i in range(n, 0, -1):
            print(" "*(n-i) + ("*"*(2*i-1)) + (" "*(n-i)))


    def nine(self, n):
        for i in range(0,n,1):
            print(" "*(n-i-1) + ("*"*(2*i+1)) + (" "*(n-i+1)))

        for i in range(n, 0, -1):
            print(" "*(n-i) + ("*"*(2*i-1)) + (" "*(n-i)))

    def ten(self, n):
        for i in range(0,n,1):
            print(" "*(n-1) + ("*"*(i+1)) + (" "*(n-i+1)))

        for i in range(n, 0, -1):
            print(" "*(n-1) + ("*"*(i-1)) + (" "*(n-i)))


    def eleven(self, n):
        for i in range(1, n+1):
            t = ("0") if i%2==0 else ("1")

            if (i >= 2):
                t = t + " " + p
            p = t

            print(t)

    def twelve(self, n):
        # for i in range(1, n+1):
        #     for j in range(i):
        #         print(str(j+1) + (" " * (n-i)) + str(j+1), end="")
        #     print("")
        pass

    def thirteen(self, n):
        count = 1
        for i in range(n+1):
            for _ in range(i):
                print(count , " ", end="")
                count+=1
            print("")

    def fourteen(self, n):
        for i in range(1, n+1):
            a = 65
            for _ in range(i):
                print(chr(a), end="")
                a+=1
            print("")

    def fifteen(self, n):
        for i in range(n, 0, -1):
            a = 65
            for _ in range(i):
                print(chr(a), end="")
                a+=1
            print("")

    def sixteen(self, n):
        a = 64
        for i in range(1, n+1):
            a+=1
            for j in range(i):
                print(chr(a), end="")
            print("")

pattern = Patterns()

# print("pattern 1: \n")
# pattern.one(5)

# print("\n pattern 2: \n")
# pattern.two(5)

# print("\n pattern 3: \n")
# pattern.three(5)

# print("\n pattern 4: \n")
# pattern.four(5)

# print("\n pattern 5: \n")
# pattern.five(5)

# print("\n pattern 6: \n")
# pattern.six(5)
# print("\n pattern 7: \n")
# pattern.seven(5)

# print("\n pattern 8: \n")
# pattern.eight(5)

# print("\n pattern 9: \n")
# pattern.nine(5)

# print("\n pattern 10: \n")
# pattern.ten(5)

# print("\n pattern 11: \n")
# pattern.eleven(5)


pattern.fifteen(4)
