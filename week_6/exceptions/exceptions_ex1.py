
# #q1

# def safe_int(s: str) -> int:
#     try:
#         return int(s)
#     except (ValueError, TypeError):
#         return None

# #2

# def safe_divide(a: int, b: int) -> float:
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "untefined"
    

# #q3

# def read_first_line(path: str):
#     try:
#         with open(path, 'r') as f:
#             return str(f.readline())
#     except (PermissionError, FileNotFoundError):
#         return None

# #q4


# from typing import Any
# def get_value(d: dict, key: str) -> Any:
#     try:
#         return d[key]
#     except KeyError:
#         "missing"

# #q5

# def parse_ints(values: list) -> list:
#     nums = []
#     for num in values:
#         try:
#             nums.append(int(num))
#         except (ValueError, TypeError):
#             pass
#     return nums

# #q6

# def get_age(age: int) -> int:
#     if 0 <= age <= 150:
#         return age
#     else:
#         raise ValueError()

# # q7

# class InsufficientFoundsError(Exception):
#     pass

# def withdraw(balance: int, amount: int) -> int:
#     if (balance - amount) >= 0:
#         return balance - amount
#     raise InsufficientFoundsError

# #q8

# def retry(func, n):
#     for i in range(n):
#         try:
#             return func()
#         except Exception as e:
#             pass
#     raise e

# #q9

# def count_errors(funcs: list) -> int:
#     count = 0
#     for f in funcs:
#         try:
#             f()
#         except Exception as e:
#             count += 1
#     return count

# #q10


# def load_config(path: str) -> int:
#     try:
#         with open(path, 'r') as f:
#             return int(f.readline())
#     except Exception as e:
#         raise RuntimeError("faild to load config") from e
