def is_leap_year():
    y=int(input("Enter a year: \n"))
    if 1990 <= y <= (10**5):
        return y%4==0

result = is_leap_year()
print(result)