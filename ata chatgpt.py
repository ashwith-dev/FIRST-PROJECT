# Program to count the number of digits,
# find the sum of digits, and reverse the number

# Input from the user
number = int(input("Enter a positive integer: "))

original_number = number   # store original number
count = 0
digit_sum = 0
reverse = 0

# Loop until number becomes 0
while number > 0:
    digit = number % 10           # get the last digit
    number = number // 10         # remove the last digit

    count += 1                    # count digits
    digit_sum += digit            # add to sum
    reverse = reverse * 10 + digit  # build reverse

# Output the results
print("Number of digits:", count)
print("Sum of digits:", digit_sum)
print("Reverse of", original_number, "is", reverse)
