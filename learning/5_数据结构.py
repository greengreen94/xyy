# 数据结构（列表list，元组tuple，集合，字典dictionary）

# 列表的创建
# 用方括号[]定义列表，列表中的每个成分都可以是任意类型的
letters = ["a", "b", "c"] # 字符串列表，还有数字列表、布尔值列表
matrix = [[0, 1], [2, 3]] # 列表的列表，列表的每个成分本身都是一个列表（矩阵，二维列表）
zeros = [0] * 5 # 创建有5个0的列表，[0]是只有一个成分（0）的列表，用星号*重复列表中的成分
combined = zeros + letters # 用加号+连接多个列表
numbers = list(range(20)) # 创建从0到19的列表，list()函数需要可迭代变量，并将其转换为列表；range()函数返回range对象
chars = list("Hello World") # 原始字符串中的每个字符都是列表中的一个成分，包括空格
print(len(chars)) # 使用len()函数获得列表中的成分数

# 获取列表中的数据
letters = ["a", "b", "c", "d"]
print(letters[0]) # 用方括号获得列表中的每个成分，类似字符串
letters[0] == "A" # 修改列表中的成分
print(letters[0:3]) # 返回一个新列表，其中包含原始列表中的前三个成分
print(letters[:3])
print(letters[::2]) # 返回列表中每x个成分，此处步长x=2
# ::
numbers = list(range(20))
print(numbers[::2]) # 得到所有的偶数
print(numbers[::-1]) # 返回原始列表中的所有成分但顺序相反

# 解包列表（把列表解压缩成多个变量，取出列表中的数据）
numbers = [1, 2, 3]
first = numbers[0]
second = numbers[1]
third = numbers[2]
first, second, third = numbers # 与上面三行等价，解压列表，更干净、更优雅
# 赋值运算符左侧的变量数应该等于列表中成分个数，否则会报错
numbers = [1, 2, 3, 4, 4, 4, 4, 4] # 如果列表中成分很多，只需要前2个
first, second, *other = numbers # 既有解压又有压缩
print(first)
print(other) # 返回一个列表，被星号*打包了
print(*other) # 返回多个成分，被星号*解包了
numbers = [1, 2, 3, 4, 4, 4, 4, 9]
first, *other, last = numbers # 如果列表中成分很多，只需要第一个和最后一个
print(first, last)
print(other)

# 循环列表
# 元组
letters = ["a", "b", "c"]
for letter in letters:
    print(letter)
# 获得每个成分的索引（enumerate()函数）
for letter in enumerate(letters): # enumerate()函数返回enumerate对象，可迭代；每次迭代中，enumerate对象会返回一个元组（元组类似于列表，但是是只读的）
    print(letter) # 元组中的第一项是索引，第二项是该索引对应的成分
for letter in enumerate(letters):
    print(letter[0], letter[1])

letters = ["a", "b", "c"]
items = (0, "a")
index, letter = items
for index, letter in enumerate(letters):
    print(index, letter)

letters = ["a", "b", "c"]
# Add
letters.append("d")
letters.insert(0, "-")
# Remove
letters.pop(0)
letters.remove("b")
del letters[0:3]

letters = ["a", "b", "c"]
letters.count("d")
if "d" in letters:
    print(letters.index("d"))

numbers = [3, 51, 2, 8, 6]
numbers.sort(reverse=True)
print(sorted(numbers, reverse=True))

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]
def sort_item(item):
    return item[1]

items.sort()
print(items)

price = []
for item in items:
    price.append(item[1])
print(prices)