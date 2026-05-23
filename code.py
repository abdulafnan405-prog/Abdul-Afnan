# population = 10000
# pop =10000
# for i in range (2011,2021):
#   pop = 0.1*pop12
#   population = population+0.1*population
#   print(i,"me itne loga bade-->",pop,"!""Total->",population)
# lower = int(input('enter lower range'))
# upper = int(input('enter upper range'))

# for i in range(lower,upper+1):
#   for j in range(2,i):
#     if i%j == 0:
#       break
#   else:
#     print(i,"prime number") 


# s = "hello world"
# print(s[-1:-5:-2])

# ## Common Functions
# - len
# - max
# - min
# - sorted


# a = "hello world"
# len(a)  # 11
# max(a)  # 'w'
# min(a)  # ' '
# sorted(a)  # [' ', 'd', 'e', 'h', 'l', 'l', 'l', 'o', 'r']    

# ## Capitalize/Title/Upper/Lower/Swapcase
# a = "hello world"
# print(a.capitalize( ))  # Hello world
# print(a)
# print(a.title( )) # Hello World
# print(a.upper( )) # HELLO WORLD
# print(a.lower( )) # hello world   
# print(a.swapcase( )) # HELLO WORLD

# ## Count/Find/Index
# b = "afnan bhai"
# "Good moring".find("mo")
# "heloow world".index("d")
# "ther u go".count("go")

# "hi my name is afnan".startswith("hi") # True
# "hi my name is afnan".endswith("name") # False
# name="afnan"
# country= "india"
# 'what is your {0} and where are you from {1}'.format(name,country) # what is your name and where are you from

# name = 'aman'
# gender = 'male'
# print('Hi my name is {1} and I am a {0}'.format(gender,name))


# # isalnum/isalpha/isdigit/isidentifier
# "afnan123".isalnum() # True
# "afnan".isalpha() # True      
# "123".isdigit() # True
# "my_name_is_afnan".isidentifier() # True

# ## Split/Join
# print("hi my name is afnan".split()) # ['hi', 'my', 'name', 'is', 'afnan']
# print("/".join(['hi', 'my', 'name', 'is', 'afnan'])) # hi/my/name/is/afnan

# # replace / strip
# print("there u go again".replace('go','in')) # there u in again
# print("   hello world   ".strip()) # "hello world"

# # Find the length of a given string without using the len() function
# s = input("Enter a string: ")
# counter = 0
# for i in (s):
#   counter +=1

# print("The length of the string is:", counter)  

# Extract username from a given email. 
# Eg if the email is afnan405@gmail.com 
# then the username should be afnan405
# email = input("enter the email: ")
# position = email.index("@")

# user =email[0:position]
# print("The user name is:", user)


# Write a program which can remove a particular character from a string.
s = input('enter the string')
term = input('what would like to remove')

result = ''

for i in s:
  if i != term:
    result = result + i

print(result)