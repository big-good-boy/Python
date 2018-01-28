# for number in range(1,21):
# 	print(number)

# numbers = list(range(1,1000001))
# for number in numbers:
# 	print(number)

# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# for number in range(1,20,2):
# 	print(number)

# for number in range(3,31,3):
# 	print(number)

list_numbers = []
# for number in range(1,11):
# 	number = number**3
# 	list_numbers.append(number)

[list_numbers.append(number**3) for number in range(1,11)]

for cube in list_numbers:
	print(cube)

print("\nThe first three items in the list are:")
print(list_numbers[:3])

print("\nThree items from the list are:")
print(list_numbers[3:6])

print("\nThe list three items in the list are:")
print(list_numbers[-3:])