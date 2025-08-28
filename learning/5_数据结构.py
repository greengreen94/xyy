# 数据结构（列表list，元组tuple，集合，字典dictionary）

# 列表的创建
# 用方括号[]定义列表，列表中的每个对象都可以是任意类型的
letters = ["a", "b", "c"] # 字符串列表，还有数字列表、布尔值列表
matrix = [[0, 1], [2, 3]] # 列表的列表，列表的每一项本身都是一个列表（矩阵，二维列表）
zeros = [0] * 5 # 创建有5个0的列表，[0]是只有一个对象（0）的列表，用星号*重复列表中的项
combined = zeros + letters # 用加号+连接多个列表
numbers = list(range(20)) # 创建从0到19的列表，list函数需要可迭代变量，并将其转换为列表；range函数返回range对象
chars = list("Hello World") # 原始字符串中的每个字符都是列表中的一个项，包括空格
print(len(chars)) # 使用len函数获得列表中的项目数

#
letters = ["a", "b", "c", "d"]
print(letters[0]) # 用方括号获得列表中的每一项
letters[0] == "A" # 修改列表中的项
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