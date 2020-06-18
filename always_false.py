#function named always_false() that has one parameter named num.
#function will return False no matter what number is stored in num.

def always_false(num):
  if (num >= num) or (num <= num):
    return False

print (always_false(0))
# should print False
print (always_false(-1))
# should print False
print (always_false(1))
# should print False
