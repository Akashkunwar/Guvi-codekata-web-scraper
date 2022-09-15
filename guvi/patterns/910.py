# QID: 910
# 
# Write a code to generate a alphabet pyramid pattern.
# 
# Given an integer R indicates number of rows.Where 1<=R<=26.
# 
# 
# Print the alphabet pyramid pattern according to the given integer R.
# 
# 
# Sample Input : 
# 5
# 
# Sample Output : 
#     A
#    ABC
#   ABCDE
#  ABCDEFG
# ABCDEFGHI
# 


# Solution:


def pattern(n):
    c = 65
    for i in range(1, n+1):
        for j in range(n-i):
            print(' ', end = "")
        for j in range(2*i - 1):
            print(chr(c+j), end = "")
        print()
n = int(input())
pattern(n)