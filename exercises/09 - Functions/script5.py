def max_number(*numbers):
    max_number = numbers[0]
    for number in numbers[1:]:
        if number > max_number:
            max_number = number
    return max_number
print(max_number(1,-1,12,111))