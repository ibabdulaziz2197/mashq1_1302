# 1.1
my_tuple = (5, 10, 15, 20)


print("Tuple uzunligi:", len(my_tuple))


print("Uchinchi element:", my_tuple[2])

print("15 bor mi", 15 in my_tuple)



# 1.2
colors = ('red', 'blue', 'green')

colors = list(colors)

colors.append('yellow')

colors.remove('blue')

colors.sort()


# 1.3
numbers = (3, 7, 2, 9, 4)

a = sum(numbers)


if a % 2 == 0:
    print("juft")

else:
    print("toq")

print(a)


# 1.4
items = (1, 2, 2, 3, 3, 4, 1)

a = list(items)
print(a.sort())
print(a)


# 1.5
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

new_tuple = tuple1 + tuple2
print(new_tuple)

print(len(new_tuple))
