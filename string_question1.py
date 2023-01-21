def q1(customer_str):
    first_letter = customer_str[0]
    if len(customer_str) % 2 == 1:
        middle_letter_index = len(customer_str) // 2
    if len(customer_str) % 2 == 0:
        middle_letter_index = (len(customer_str) // 2) - 1

    middle_letter = customer_str[middle_letter_index]

    last_letter_index = len(customer_str) - 1

    last_letter = customer_str[last_letter_index]
    return first_letter + middle_letter + last_letter




#test
print(q1("James"))
print(q1("Jama"))