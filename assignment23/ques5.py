'''Question 5
Create a function that returns the mean of all digits.
Examples
mean(42) ➞ 3

mean(12345) ➞ 3

mean(666) ➞ 6
Notes
•	The mean of all digits is the sum of digits / how many digits there are (e.g. mean of digits in 512 is (5+1+2)/3(number of digits) = 8/3=2).
•	The mean will always be an integer.'''

def mean(num):
    digits = [int(digit) for digit in str(num)]
    return sum(digits) // len(digits)

print(mean(42))
print(mean(12345))
print(mean(666))