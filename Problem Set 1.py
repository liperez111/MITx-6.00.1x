"""
Problem set 1
"""

"""
Problem 1

Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""
s = 'azcbobobegghakl'
y = 0
for i in str(s):
    if i in ["a", "e", "i", "o", "u"]:
        y = y + 1

print("Number of vowels: " + str(y))

"""
Problem 2
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2

"""
s = 'azcbobobegghakl'
y = 0

for i in range(0, len(s)):
    if s[i:i + 3] == "bob":
        y = y + 1

print("Number of times bob occurs is: ", str(y))

"""
Problem 3
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""

s = 'gmqbrcdmrxslqiycca'
y = s[0]
longest = ""
for i in range(0, len(s) - 1):
    if s[i + 1] >= s[i]:
        y = y + s[i + 1]
        if y == s:
            longest = y
            break
    else:
        if len(y) > len(longest):
            longest = y
            y = s[i + 1]
        else:
            y = s[i + 1]
print("Longest substring in alphabetical order is: " + str(longest))

#removing testing











