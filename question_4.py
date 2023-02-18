'''
4. Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.

Example:
  s1 = "America"
  s2 = "Japan"

  Expected output: "AJrpan"

  1, find length of s1 and s2 l1 and l2
  2, get first index of s1 and s2
  3, find the middle index of s1 and s2
  4, get the last index of s1 and s2
  5, return combine first + middle + last

'''

def combine_first_middel_last(s1, s2):
    l1 = len(s1)
    l2 = len(s2)

    fl_s1 = s1[0]
    fl_s2 = s2[0]

    ml_s1 = s1[l1//2]
    ml_s2 = s2[l2//2]

    ll_s1 = s1[l1-1]
    ll_s2 = s2[l2-1]

    return fl_s1 + fl_s2 + ml_s1 + ml_s2 + ll_s1 + ll_s2

a = combine_first_middel_last("America", "Japan")
print(a)
