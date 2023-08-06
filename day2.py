# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
#input is 28 output should be 2 + 8 = 10, input 51 output => 5 + 1 = 6
num_str = str(two_digit_number)
print(int(num_str[0]) + int(num_str[1]))

#--------------------------------------------------------------------------
data = "balaji"
print(data[-1])
print(data[2])
print(data[2:5])
print(data[2:-1])
print("your name is "+input("what is your name ? \n"))
print("hello \"vijay\"")
#interger 
num = 3332
#float
num_float = 889.4
#boolean
boolean = True
False
#instead of , we can use _ 
num = 123_465_567 
#above wil be treated as 
123456
#num with _ of type float
12_45.89
123_98.77
#type casting or type conversion 
int("909")
float("908.77")
print(float(78))
print(str(89))
print(str(999.98))

#type() is used to print the type of the variable
print(type(898))
print(type(898.87))
print(type("989"))
print(type(True))

new_num = 98
#print("number is " + 98) will throw error because we are trying to concatinate string with number: right way to do this
#print("number is " + str(98))

#operator precendance 
#PEMDAS
#P - peranthesis - ()
#E - exponent - **
#M - multiplication - *
#D - division - /
#A - addition - +
#S - subtraction - -

#multipication ad division has same priority
#addition and subtraction has same priority  
#calculation happens from left to right
print(3 * 3 + 3 / 3 - 3)
#calculation happens from left to right
#3*3 = 9 
#3/3 = 1
#9 + 1 = 10
#10 - 1 = 9
#final answer 9


#BMI calculator
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#BMI formula => weight (KG) / height^2 (m^2)
print(int(float(weight) / float(height)**2))


#fstrings
f_num = 998
f_num1 = 1
f_str = "vijay"
f_float = 879.987
f_bool = False
print(f" print diffrent datatypes {f_num}, {f_num+f_num1} , {f_str} , {f_float} , {f_bool}")


#age calculator

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
agint = 90 - int(age)
days = agint*365
weeks = agint*52
mnts = agint*12

print(f"You have {days} days, {weeks} weeks, and {mnts} months left.")


#bill spiliting calculator
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("welcome to the tip calculator")
amt = float(input("What was the total bill? $"))
tip = float(input("what percentage of tip would you like to add 10, 12, and 15? "))
tip_cal = (amt * tip) / 100
amt += tip_cal
spilt = int(input("How many people to spilit the bill ? "))
spilt_tot = round((amt / spilt) , 2)
decimal_2_point = "{:.2f}".format(spilt_tot)
print(f"each person pays {decimal_2_point}")
