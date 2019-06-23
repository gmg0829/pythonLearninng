# Our numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Function that filters out all numbers which are odd
def filter_odd_numbers(num):

    if num % 2 == 0:
        return True
    else:
        return False

filtered_numbers = filter(filter_odd_numbers, numbers)

for i in filtered_numbers:
     print(i)  