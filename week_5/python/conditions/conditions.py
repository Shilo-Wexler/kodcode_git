# # q 1

# age = int(input("Enter your age: "))


# if  age <= 0 or age >= 120:
#     print("Invalid")
# elif 0 < age <= 12:
#     print("Child")
# elif 13 <= age <=17:
#     print("Teen")
# else:
#     print("Adult")


# #q 2

# VOWEL = ('a', 'e', 'i', 'o', 'u')

# car = input("Please enter a English car: ").lower()

# if car in VOWEL:
#     print("Vowel")
# elif  'a' <= car <= 'z':
#     print("Consonant")
# else:
#     print("Invalid")
# #q 3

# entry_premit = False
# age = int(input("Please enter your age: "))
# if age > 16:
#     if 18 < age < 22:
#         entry_premit = True
#     else:
#         vip = input("do you have vip card? (yes/no): ").lower()
#         entry_premit = vip == 'yes' and age > 18
#     if entry_premit:
#         print("you in!")
    
# #q 4

# PASSWORD = 12345678

# password = input("Enter your password: ")

# if password == PASSWORD:
#     print("Access Granted")
# elif (len(password) < 8 ):
#     print("Too short")
# else:
#     print("Wrong password")

# #q 5

# #q 6

# DEFOULT_NAME = 'Anonimus'
# name = input("Enter your name: ")
# print(f"Hello {name or DEFOULT_NAME}")

# #q 8

# x1 = int(input("Enter first num"))
# x2 = int(input("Enter secund num"))
# x3 = int(input("Enter third num"))

# print((x1 >= 0) + (x2 >= 0) + (x3 >= 0))

# #q 10

# score = int(input("Enter a score from 0 to 100: "))

# print("A" * (score >= 90) , "B"  * (89 >= score >= 80), "C" * (70 <= score <= 79), "F" * (score < 70 ))
