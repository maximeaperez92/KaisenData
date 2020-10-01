import re

# Question 1
#txt = "Comment t'apelles-tu ?"
#x = re.search("a", txt) # "a" is equivalent to "a[b]*"

# Question 2
#txt = "Je m'apelle Maxime"
#x = re.search("[A-Z][a-z]", txt)

# Question 3
#txt = "areerb"
#x = re.search("a\w+b", txt) # "\w+" equivalent to "([a-z]+|[A-Z]+|[0-9])"

# Question 4
#txt = "abzolutely"
#x = re.search("^([a-y]+|[A-Y]+)z([a-y]+|[A-Y]+)$", txt)

# Question 5
#txt = "I have, no more ... inspiration ! This is crazy"
#print(re.split(', | [.]+ | !', txt))

# Question 6

# English :
#txt = "Listen carefully ! I need to go quickly to the hospital."
#for m in re.finditer("\w+ly", txt):
#    print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))

# French :
#txt = "Ecoute attentivement ! Tu ne continueras pas à faire tes bétises impunément"
#for m in re.finditer("\w+ment", txt):
#    print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))

# Question 7
txt = "I am born the 08/12/1999 with the french format and 12/08/1999 in english format"
for m in re.finditer("([0-3][0-9]/[0-1][0-9]/[0-9]+)|([0-1][0-9]/[0-3][0-9]/[0-9]+)", txt):
    print(m.group(0))
# There are no limits on the date, it can depass 9999, can be useful in fantasy romans.
# If we want to stick with date of now we remplace "[0-9]" by "[0-2][0-9][0-9][0-9]"

'''
# Vérification regex
if x:
    print("This match !")
else:
    print("There is no match !")
'''