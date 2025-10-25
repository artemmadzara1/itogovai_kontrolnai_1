# import random
#2 задача
# numbers=list(map(int, input("Введите числа через пробел").split()))
#
# positive_count = 0
# negative_count = 0
#
# for num in numbers:
#     if num > 0:
#         positive_count += 1
#     elif num < 0:
#         negative_count += 1
#     elif num == 0:
#         positive_count +=1
# print(f"Количество положительных чисел: {positive_count}")
# print(f"Количество отрицательных чисел: {negative_count}")
# 3 задание
# n = list(map(int,input("ведите какие рандомные числа будут использаваны только(2) ").split()))
# b = int(input("введите количество сколько чисел будет выведено "))
#
# list_1=[random.randint(n[0], n[1]) for _ in range(b)]
# multiple_3=0
# for i in list_1:
#     print(i)
#     if i % 3 == 0:
#         multiple_3 +=1
# print(multiple_3)
