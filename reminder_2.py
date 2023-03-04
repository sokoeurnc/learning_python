arr_number = [1,20,9,2,9,3,7,4,6,5]

temp = arr_number[0]
arr_number[0]= arr_number[1]
arr_number[1]=temp
print(arr_number)

arr_number.append(100)
print(arr_number)

a = arr_number[len(arr_number)-3:]
print(a)

new_array = [99]


arr_number = [99] + arr_number
print(arr_number)

index = 0
while True:
    print(arr_number[index])
    index = index + 1
    if index == len(arr_number):
        break
