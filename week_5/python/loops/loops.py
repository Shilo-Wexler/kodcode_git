# #q1
# for i in range(1, 11):
#     if i % 2 == 0:
#         continue

#     print (i)

#     if i == 7:
#         break

# #q2

# PASSWORD = '1234'

# while True:
#     password = input("enter your password")
#     if password == PASSWORD:
#         break
#     print("Try agein")
# print("Welcome!")

#q3

# prodacts = []

# while True:
#     prodact = input("enter prodact name or 'done' to quit: ").lower()
#     if prodact == "done":
#         break
#     prodacts.append(prodact)
# for item in prodacts:
#     print(item)

##q4

# VOWELS = ('a', 'e', 'i', 'o', 'u')

# word = input("enter a word: ").lower()

# count = 0

# for c in word:
#     if c in VOWELS:
#         count +=1
# print(count)

# #q5
# for i in range(1,6):
#     for j in range(1,6):
#         print(f"{i} x {j} = {i*j}")


# #6

# word = input("enter a word: ")
# new_word = ''
# for i in range(len(word)-1, -1, -1):
#     new_word += word[i]
# print(new_word)

# #q7

# num = int(input("Enter a num: "))
# count = 0

# while num > 0:
#     if num % 2 == 0:
#         count +=1
#     num = num//10
# print(count)

# #q8

# word = input("please enter a word ")
# new_word = ""

# for i in word:
#     new_word += i *2
# print(new_word)

# #q9

# max_num = 0


# while True:
#     user_choice = int(input("Please enter a positive num: "))
#     if user_choice > max_num:
#         max_num = user_choice
#     elif user_choice == 0:
#         break
# print(max_num)

# #q10

# word = input("please enter a word: ")

# print(word.isalnum())

# #q11

# num = int(input("please enter a num: "))
# result = 0
# base_ten = 10

# while num > 0:
#     result *= base_ten
#     result += num % 10
#     num = num // 10
# print(result)


