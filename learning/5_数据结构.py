# 数据结构（列表，元组，集合，字典）
letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0]*5
combined = zeros + letters
numbers = list(range(20))
chars = list("Hello World")
print(len(chars))

letters = ["a", "b", "c", "d"]
letters[0] == "A"
print(letters[0:3])
print(letters[::2])

numbers = list(range(20))
print(numbers[::-1])
numbers = [1, 2, 3]
first = numbers[0]
second = numbers[1]
third = numbers[2]
first, second, third = numbers
numbers = [1, 2, 3, 4, 4, 4, 4, 4]
first, second, *other = numbers
print(first)
print(other)
numbers = [1, 2, 3, 4, 4, 4, 4, 9]
first, *other, last = numbers
print(first, last)
print(other)

letters = ["a", "b", "c"]
for letter in enumerate(letters):
    print(letter[0])