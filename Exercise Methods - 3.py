num1 = 1122334455666
num2 = "yuceltan"
num3 = 56456456
num1_str =str(num1)
print(type(num1_str),len(num1_str),num1_str[2],num1_str[3:6])
if num2.isdigit() == False:
    print("number 2 is a string")
elif num2.isdigit() != True:
    print("number 2 is not a string")
else:
    print("unvalid process")


try:
    value = int(num3)
except ValueError:
    print("it was a string, not an int")
    pass  # it was a string, not an int.








#there is no num2 or num3

"""to convert a number to string we can use str() function this is called casting

cast num1 to string and assign to num1_str+
check the length of the string+
get the third element of string (the one in the 3rd order)+
get the 3-5 elements of string (both inclusive) by string slicing+
check if num2 in string (cast if necessary)+
check if num3 in string (cast if necessary)+
concatenate 0 to the string from left and assign to string_with_0
get the characters of string_with_0 from start to position 4 (end point exclusive)
get the characters of string_with_0 from position 5 until the end
use negative indexing to reach the "567" string_with_0"""