print True
print False


print (True and False)  # -> False
print (True or False)   # -> True


small_number = 2
big_number = 100

print small_number > big_number     # False
print small_number < big_number     # True
print small_number == big_number     # False
print small_number != big_number     # True
print small_number is big_number     # False
print id(small_number), id(big_number)
print small_number is not big_number     # True

print "small_number > big_number: ", small_number > big_number  # -> False
