'''
1, find the index of :
2, return url[:index]
'''

def parse_protocol(url):

    index = 0
    while True:
        if url[index] == ":":
            break
        index = index + 1
    return url[:index]

a = parse_protocol("mailto://abc.gh")
print(a)






def parse_port(url):
    index = 0
    number_of_coloun_found = 0
    while True:
        a = url[index]
        if a ==":":
            number_of_coloun_found = number_of_coloun_found + 1
            if number_of_coloun_found == 2:
                break

        index = index + 1

    index_of_second_colon = index
    while True:
        if url[index] == "/":
            break
        index = index + 1
    return url[index_of_second_colon +1 : index]



b = parse_port("https://vk:80/videoplay")
print(b)