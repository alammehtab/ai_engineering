# problem
# If two keys are same in a dictionary what will happen?

# solution
my_dict = {"a": 1, "b": 2, "a": 3}  # Duplicate key 'a'

print(my_dict)
# the last occurrence of the duplicate key will overwrite the previous value associated with that key
