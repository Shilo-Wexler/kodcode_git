# # q1

# def is_even(n: int) -> bool:
#     """
#     Chacks if the n is even.

#     Args:
#         n: the num for chacking
#     Returns:
#         true: if n is even. false: otherwise.
#     """
#     return n % 2 == 0

# #q2

# def factorial(n: int) -> int:
#     result = 1
#     for i in range(n):
#         result *= i+1
#     return result

# #q3
# VOWELS = ('a', 'i', 'e', 'u', 'o')

# def count_vowels(s: str) -> int:
#     count = 0
#     for c in s:
#         count += 1 if c.loewr() in VOWELS else 0
#     return count

# #q4

# def reverse_string(s: str) -> int:
#      return "".join([c for c in reversed(s)])

#q5

# def find_max(lst: list[int]) -> int:
#     max_n = lst[0]
#     for n in lst:
#         max_n = n if n > max_n else max_n
#     return max_n

# #q6

# def celsius_to_fahrenheit(c: float) -> float:
#     return c * 1.8 + 32


##7

# def is_palindrome(s: str) -> bool:
#     for i in range (len(s)//2):
#         if s[i] != s[len(s)-1 - i]:
#             return False
#     return True

# #q8

# def even_lst(lst: list) -> list:
#     return [n for n in lst if n % 2 == 0]

# #9

# def chack_anagrams(s1: str, s2: str) -> bool:
#     lst_c1 = sorted([c.lower() for c in s1])
#     lst_c2 = sorted([c.lower() for c in s2])
#     if len(lst_c1) != len(lst_c2):
#         return False
#     for i in range(len(lst_c1)):
#         if lst_c1[i] != lst_c2[i]:
#             return False
#     return True

# #q10

# def count_words(s: str) -> dict:
#     sentence = s.lower().split()
#     words = dict()
#     for word in sentence:
#         if word in words:
#             words[word] += 1
#         else:
#             words[word] = 1
#     return words

# #q11

# def calculate_resource_drain(cost: float, waste_factor: float) -> float:
#     return cost * waste_factor

# def get_net_resource(cost: float, waste_factor: float) -> float:
#     return cost - calculate_resource_drain(cost, waste_factor)

# #q12

# def intercept_length(packet: str) -> int:
#     return len(packet.encode('utf-8'))

# def verify_transmission(packet: str) -> str:
#     return f"Intercept packet contains {intercept_length(packet)} bytes of data"


# #q13

# import math

# def convert_to_decibels(signal_strength: float) -> float:
#     return 20 * math.log10(signal_strength)

# def is_threat_detected(signal_strength: float) -> float:
#     return convert_to_decibels(signal_strength) > 90

# #q14

# def get_fuel_surcharge(distance: float) -> float:
#     return (distance / 10) * 8 * 0.17


# def get_hazard_pay(distance: float) -> float:
#     return get_fuel_surcharge(distance) * 0.5
    

# def calculate_mission_cost(distance: float) -> float:
#     return distance \10 * 8 + get_fuel_surcharge(distance) + get_hazard_pay(distance)