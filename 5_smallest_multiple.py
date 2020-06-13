###############################################################################
#
# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?
#
###############################################################################

import time

user_number = int(input("Find the smallest positive number that is evenly divisible by all numbers from 1 to what number? "))
timer = time.time()
max_number = user_number
test = max_number
total_factors = [1]
temp_factors = [1]
test_number = 2
final_product = 1

def reset_temp_values():
    test_number = 2
    temp_factors = [1]

def remove_duplicate_factors():
    for each_factor in total_factors:
        if each_factor in temp_factors:
            temp_factors.remove(each_factor)

def print_all_factors():
    print("\n")
    print("The valuse in total_factors: \n")
    for x in total_factors:
        print(x)

def calculate_product():
    calc_product = 1
    for x in total_factors:
        calc_product = calc_product * x
    return calc_product
 
while max_number > 1:
    test = max_number
    while test > 1:
        if test % test_number == 0:
            test = test / test_number
            temp_factors.append(test_number)
            test_number = 2
        else:
            test_number = test_number + 1
                
    remove_duplicate_factors()

    total_factors = total_factors + temp_factors
    max_number = max_number - 1

    reset_temp_values()


final_product = calculate_product()

print("The smallest positive number that is evenly divisible by all of the numbers from 1 to {} is {}".format(user_number, final_product))
print("Time = {}".format(round(time.time() - timer, 6)))
