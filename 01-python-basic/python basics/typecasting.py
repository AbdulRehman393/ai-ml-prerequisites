#Typecasting = the process of converting a varible from one date type to anothher
#              str(), int(), float(), bool()

name = "Abdul Rehman"
age = 25
gpa = 3.2
is_student = True

# You could get tge datatype of variable or value by using the type function
print(type(name))


gpa = int(gpa)
print(gpa)

age = float(age)
print(age)

age = str(age)
print(age)

# age +=1 here we will get type error We can only concatenate strings, not integers to a string
# if we will do like following , We will be using concatenation
age += "1"  # Since , We are working with strings, the result will be 221
print(age)


