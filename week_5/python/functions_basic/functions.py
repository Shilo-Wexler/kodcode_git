# #q5

# def repeat_sum_digits(n: int) -> int:
#     num = sum_digits(n)
#     while num >= 10:
#         num = sum_digits(num)
#     return num


# def sum_digits(n: int) -> int:
#     num = 0
#     while n > 0:
#         num += n % 10
#         n = n // 10
#     return num

# #q6

# def sum_digits(n: int) -> int:
#     sum = 0
#     while n > 0:
#         sum += 1
#         n = n // 10
#     return sum


# #q8

# def moveZero(lst: list) -> None:
#     for n in lst:
#         if n == 0:
#             lst.remove(0) 
#             lst.append(0)


# #q9

# def print_data(lst: list) -> None:
#     max , min = lst[0], lst[0]
#     sum = 0
#     for n in lst:
#         max = n if max < n else max
#         min = n if min > n else min
#         sum += n
#     print(max , min , sum /len(lst))

#q10

