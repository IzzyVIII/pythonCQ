#   ****Note: I did the new prework and the questions with the AI sensei when I was in Kekembas for a hot second. Then I did these questions when I joined the Rangers****

#Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as below. def hello_name(user_name):

greeting="Hello "
username="Liz"
print(greeting + username)

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():

def first_odds():
  num = list(range(1,101,2))
  if(100 % 2) == 0:
       print(num)

first_odds()

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below. 

a_list=[23,8,13,83,4,9,33]
def max_num_in_list(a_list):
    max = a_list[0]
    
    for number in a_list:
        if number>max:
            max=number
    return max # (I think this is wrong but not sure why nothing prints or shows an error.) 

# Question 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. 
# The return should be boolean Type (true/false). def is_leap_year(a_year):

def is_leap_year():
    a_year = 2025
    if a_year / 4 == 4:
        print(True)
    elif a_year / 100 == 100:
        print(True)
    else: a_year / 400 == 400
    print(False)
   
is_leap_year()

# Question 5
# Write a function to check to see if all numbers in the list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type. def is_consecutive(a_list):

def is_consecutive(a_list):     
    a_list = list[1,2,3,4,5,6,7,8,9]
print(1 == (+1))