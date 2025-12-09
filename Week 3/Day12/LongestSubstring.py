# Longest Substring Without Repeating Characters
def longest_unique_substring(s):
    seen = set()
    left = 0
    longest = ""

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        if (right - left + 1) > len(longest):
            longest = s[left:right+1]

    return longest

string = input("Enter a string: ")
print("Longest substring without repeating characters:", longest_unique_substring(string))
