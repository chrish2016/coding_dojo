import math

# Odd/Even
# for x in range(1, 2001):
#     if (x % 2 != 0):
#         print "the number is", x, ".", " This is an ODD number."
#     else:
#         print "the number is", x, ".", " This is an EVEN number."


# Multiply
def multiply():
    nums = [2,4,10,16]
    new_nums = []

    for i in range(0, len(nums)):
        new_nums.append(nums[i] * 5)
    
    print new_nums
multiply()