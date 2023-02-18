'''

3. Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

Example:
  s1 = "Ault"
  s2 = "Kelly"

  Expected output : "AuKellylt"

  1, find the length l of s1
  2, use l find middle index mi
  3, append s2 to s1 at index mi
  4, return result
'''

def append_str(s1, s2):
    l = len(s1)
    mi = l//2
    fh = s1[0:mi]
    lh = s1[mi:]
    s3 = fh + s2 + lh

    return s3


a = append_str("Autl", "kelly")
print(a)