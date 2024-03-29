'''Question 3. In this challenge, establish if a given integer num is a Curzon number. If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number.
Given a non-negative integer num, implement a function that returns True if num is a Curzon number, or False otherwise.
Examples
is_curzon(5) ➞ True
# 2 ** 5 + 1 = 33
# 2 * 5 + 1 = 11
# 33 is a multiple of 11

is_curzon(10) ➞ False
# 2 ** 10 + 1 = 1025
# 2 * 10 + 1 = 21
# 1025 is not a multiple of 21

is_curzon(14) ➞ True
# 2 ** 14 + 1 = 16385
# 2 * 14 + 1 = 29
# 16385 is a multiple of 29'''


def is_curzon(num):
    power_of_2 = 2 ** num
    plus_2n_1 = 1 + 2 * num
    plus_2n_1_power_of_2 = 1 + power_of_2
    
    if plus_2n_1_power_of_2 % plus_2n_1 == 0:
        return True
    else:
        return False

print(is_curzon(10))

