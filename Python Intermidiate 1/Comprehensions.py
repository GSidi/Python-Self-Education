integer_nums = [1,2,3,4,5,6,7,8,9,0]
binary_nums = ['1','2','3','4','5','6','7','8','9','0']

binary_dict = {int_nums:bin_nums for int_nums, bin_nums in zip(integer_nums,binary_nums)}

print(binary_dict)

# List
integer = [1, -1, 2, 3, 5, 0, -7]
additive_inverse = [-1*i for i in integer]
print(additive_inverse)

# Set
integer = [1, -1, 2, -2, 3, -3]
sq_set = {i*i for i in integer}
print(sq_set)