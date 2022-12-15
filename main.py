#Data Types
# WAP tp get two digit number as input and SUM-of_Digits should be output.
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
###Write your code below this line 👇
##self-written-code without subscript method
#first_num=int((int(two_digit_number))/10)
#second_num=(int(two_digit_number))%10

#With Subscrit Method
first_num=two_digit_number[0]
second_num=two_digit_number[1]
#print(first_num+" + " +second_num+" = "+str(int(first_num) + int(second_num)))
print(int(first_num) + int(second_num))
