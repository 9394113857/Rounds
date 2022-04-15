# Initializing list
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print("The original list is : " + str(test_list))

# using set() method
test_list = list(set(test_list))

# printing list after removal
print("The list after removing duplicates : " + str(test_list))
