def permute(string, answer=""):
    if len(string) == 0:
        print(answer)
        return
    
    for i in range(len(string)):
        ch = string[i]
        left_substr = string[:i]
        right_substr = string[i+1:]
        rest = left_substr + right_substr
        permute(rest, answer + ch)

s = input("Enter a string: ")
print("All permutations are:")
permute(s)
