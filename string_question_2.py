'''
2. Write a program to create a new string made of the middle three characters of an input string.

For example:

Example 1:
  str1 = "JhonDipPeta"

  Expected output: "Dip"

Example 2:
  str1 = "JaSonAy"

  Expected output: "Son"

'''

def middel_3_char(str1):
    '''
    1. find the length of string
    2. using to length to calculate middel index i
    3. we can print one index before, print middle index and print last index
    :param str1:
    :return:
    '''

    l = len(str1)
    i = l//2

    return str1[i-1:i+2]



a = middel_3_char("JaSonAy")
print(a)

