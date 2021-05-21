def func(p1, p2, *args, k, **kwargs):
    print("positions-or-keywords:...{}, {}".format(p1,p2))
    print("var_positional:..............{}".format(args))
    print("keywords:....................{}".format(k))
    print("var-keyword:.................{}".format(kwargs))


func(1, 2, 3, 4, 5, k=6, key1=7, key2=8)


#The code below is not significant here. It is related to dictionaries.
#The first code for dictionaries

# numbers = {
#     1: 'one',
#     3: 'three',
#     5: 'five',
#     7: 'seven',
#     9: 'nine',
# }
#
# print("I can count odd numbers in order")
# for key in numbers:
#     print(numbers[key])
#
# numbers[8] = 'eight'
# numbers[2] = 'two'
# numbers[6] = 'six'
# numbers[4] = 'four'
#
# print()
# print("I can count to 9 in order")
# for key in numbers:
#     print(numbers[key])
#
# # If your code relies on the keys being sorted, sort them first
# print()
# print("I really can")
# for key in sorted(numbers):
#     print(numbers[key])