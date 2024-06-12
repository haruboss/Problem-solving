def split_join(str):
    if len(str) == 0:
        return
    
    s = str.split(" ")
    
    return "-".join(s)

text = input("Please enter text: ")
result = split_join(text)
print(result)