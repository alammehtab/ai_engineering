# problem
# What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add("20")  # length of s after these operations?

# solution
print(len(s))  # length is 2 cz in python 20 and 20.0 are equal
