# Check if two strings are anagrams
def is_anagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    return sorted(str1) == sorted(str2)

s1 = "Listen"
s2 = "Silent"

if is_anagram(s1, s2):
    print(f'"{s1}" and "{s2}" are anagrams.')
else:
    print(f'"{s1}" and "{s2}" are not anagrams.')
