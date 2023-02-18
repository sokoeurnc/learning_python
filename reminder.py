arr_num = [1,2,3,4,5,6,7,8,9,10]
arr_num[0]
a = arr_num[1]
print(a)
a = arr_num[4]
print(a)

another_arr = [11,12]
c = arr_num + another_arr
print(c)

c.append(13)
print(c)

print(len(c)-1)

c.append(100)
print(c)

print(c[len(c)-1])

c[0] = 99
print(c)

c[len(c)-2] = 98
print(c)

d = c[1:5]
print(d)

d[0] = 88
print(d, c)

print(c)

c = c[:4] + c[5:]
print(c)