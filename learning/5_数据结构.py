# 数据结构（列表list[]，元组tuple()，集合set{}，字典dictionary{}）
from sys import getsizeof

from numpy.ma.core import append

# 列表的创建
# 用方括号[]定义列表，列表中的每一项都可以是任意类型的
letters = ["a", "b", "c"] # 字符串列表，还有数字列表、布尔值列表
matrix = [[0, 1], [2, 3]] # 列表的列表，列表的每一项本身都是一个列表（矩阵，二维列表）
zeros = [0] * 5 # 创建有5个0的列表，[0]是只有一项（0）的列表，用乘法运算符*重复列表中的项
combined = zeros + letters # 用加号+连接多个列表
numbers = list(range(20)) # 创建从0到19的列表，list()函数需要可迭代对象，并将其转换为列表；range()函数返回range对象
chars = list("Hello World") # 原始字符串中的每个字符都是列表中的一项，包括空格
print(len(chars)) # 使用len()函数获得列表中的项数

# 获取列表中的数据
letters = ["a", "b", "c", "d"]
print(letters[0]) # 用方括号获得列表中的每一项，类似字符串
letters[0] == "A" # 修改列表中的项
print(letters[0:3]) # 返回一个新列表，其中包含原始列表中的前三项
print(letters[:3])
print(letters[::2]) # 返回列表中每x项，此处步长x=2
# ::
numbers = list(range(20))
print(numbers[::2]) # 得到所有的偶数
print(numbers[::-1]) # 返回原始列表中的所有项但顺序相反

# 解包列表（把列表解压缩成多个变量，取出列表中的数据）
numbers = [1, 2, 3]
first = numbers[0]
second = numbers[1]
third = numbers[2]
first, second, third = numbers # 与上面三行等价，解压列表，更干净、更优雅
# 赋值运算符左侧的变量数应该等于列表中项数，否则会报错
numbers = [1, 2, 3, 4, 4, 4, 4, 4] # 如果列表中项很多，只需要前2个
first, second, *other = numbers # 既有解压又有压缩
print(first)
print(other) # 返回一个列表，被星号*打包了
print(*other) # 返回多项，被星号*解包了
numbers = [1, 2, 3, 4, 4, 4, 4, 9]
first, *other, last = numbers # 如果列表中项很多，只需要第一个和最后一个
print(first, last)
print(other)

# 元组
letters = ["a", "b", "c"]
for letter in letters: # for循环迭代列表
    print(letter)
# 获得每一项的索引（enumerate()函数）
for letter in enumerate(letters): # enumerate()函数返回可迭代的enumerate对象；在每次迭代中，enumerate对象会返回一个含2项的元组（元组类似于列表，但是是只读的）
    print(letter) # 元组中的第一项是索引，第二项是该索引对应的项
for letter in enumerate(letters):
    print(letter[0]) # 返回索引，letter是元组
    print(letter[0], letter[1]) # 解包元组，不简洁，letter[1]是每元组的第二项
# 解包元组
items = (0, "a")
index, letter = items
letters = ["a", "b", "c"]
for index, letter in enumerate(letters):
    print(index, letter)

# 向列表中添加新对象+删除现有对象
letters = ["a", "b", "c", "d", "e"]
# Add
# 在列表末尾添加对象
letters.append("f")
print(letters)
# 在特定位置添加对象
letters.insert(0, "-") # 列表开头
print(letters)
# Python中的一切都是对象，当函数是对象的一部分时，将该函数称为方法，该对象中的方法x.function
# Remove
# 删除列表末尾的项
letters.pop() # 赋值再打印，会返回被删除的末尾项
print(letters)
# 删除给定索引处的项，只能删除一项
letters.pop(0)
print(letters)
# 删除某项但不知道它的索引
letters.remove("b") # 删除第一个"b"
print(letters)
# 通过索引删除项，可以删除一项或多项
del letters[0:3]
print(letters)
# 删除列表中所有项
letters.clear()
print(letters)

# 在列表中查找给定对象的索引
letters = ["a", "b", "c"]
print(letters.index("a")) # 找到字母a的索引;查找列表中不存在的对象的索引会报错
if "d" in letters: # 检查给定的对象是否存在于列表中
    print(letters.index("d"))
print(letters.count("d")) # 返回列表中给定对象的出现次数

# 排序列表
# 对数字和字符串排序
numbers = [3, 51, 2, 8, 6]
numbers.sort() # 升序
print(numbers)
numbers.sort(reverse=True) # 降序
print(numbers)
print(sorted(numbers)) # 参数为可迭代对象iterable；返回排序的新列表，不会修改原始列表
print(sorted(numbers, reverse=True))
# 对元组排序
# 根据商品的价格对列表进行排序
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]
items.sort() # 此处sort没有作用
print(items)
def sort_item(item): # 定义函数用于排序，此处参数item代指列表中的项——元组
    return item[1] # 返回价格用于排序
# 函数的作用是接受一个元组并返回它的价格
items.sort(key=sort_item) # key参数指定排序依据，sort的第一个参数不是key，所以必须明确指定
# sort_item：加括号sort_item()表示调用函数，()内需要填入参数否则报错，不加括号sort_item表示引用函数
# sort()排序时，会对每一项调用sort_item()函数
print(items)

# lambda函数（重写sort_item函数，更干净）
# lambda函数：传递给其他函数的简单的一行匿名函数，定义函数的更简洁的方法
# 何时用：当一个函数作为另一个函数的实参，一次性的
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]
# items.sort(key=lambda parameters: expression) # lambda函数的语法，输入parameters返回expression
items.sort(key=lambda item: item[1])
print(items)

# map()映射函数（map(function, iterable, ...)：第一个参数是函数，第二个参数是一个或多个可迭代对象）
# 将列表转换成不同的形状
# 将元组列表转换成数字列表
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]
prices = []
for item in items:
    prices.append(item[1])
print(prices)
x = map(lambda item: item[1], items) # 等价于上面四行代码，更简洁
# map()函数使得items列表中每一项作为lambda函数的输入，此处lambda函数转换原始列表中的每一项
# map()函数返回map对象，map对象可迭代
for item in x:
    print(item)
prices = list(map(lambda item: item[1], items)) # map对象转换为list对象
print(prices)

# filter()过滤函数（filter(function, iterable)）
# 过滤列表，价格大于等于10的商品
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]
filtered = []
for item in items:
    if item[1] >= 10:
        # filtered.append(item[0])
        filtered.append(item)
print(filtered)
filtered = list(filter(lambda item: item[1] >= 10, items)) # 等价于上面五行代码，更简洁
# filter()函数过滤可迭代对象，保留使函数返回True的对象
# filter()函数返回filter对象，filter对象可迭代
print(filtered)

# 列表推导式
# 语法：[expression for item in iterable if condition]
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]
prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]
filtered = list(filter(lambda item: item[1] >= 10, items))
filtered = [item for item in items if item[1] >= 10]

# zip()函数
# 把两个列表组合成一个元组列表
list1 = [1, 2, 3]
list2 = [10, 20, 30]
# [(1, 10), (2, 20), (3, 30)]
print(list(zip(list1, list2))) # zip()函数返回zip对象，zip对象可迭代
print(list(zip("abc", list1, list2))) # zip()函数的参数是一个或多个可迭代对象

# 堆栈stacks（数据结构，后进先出last in first out LIFO）
# 类似于现实生活中的一叠书，浏览器浏览网站
browsing_session = []
browsing_session.append(1) # append在堆栈顶部添加项
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop() # 按下后退按钮，删除最后一项，pop删除堆栈顶部的项
print(last)
print(browsing_session)
if not browsing_session: # 检查堆栈是否为空，not运算符应用于空列表的值为布尔值True，此处意思是堆栈为空
    print("disable")
print("redirect", browsing_session[-1]) # 索引-1重定向到之前的网站，即堆栈顶部的项

# 队列queues（数据结构，先进先出first in first out FIFO）
# 类似于现实生活中的队列，
from collections import deque # collections是模块，deque是类
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft() # 移除队列的第一项，列表中没有这个方法
# 列表list只能右加append右减pop，deque给列表添加双端可添加和移除的特性，还能左加appendleft左减popleft
print(queue)
if not queue: # 此处意思是队列为空
    print("empty")

# 元组tuple（只读的列表，不能修改，括号）
# 用括号()定义元组
point = 1, 2
print(type(point)) # 也是元组，(1, 2)是元组，1,2是元组，1,是元组，1是整数，()是元组
point = (1, 2) + (3, 4) # 用加号+连接多个元组
print(point)
point = (1, 2) * 3 # 用乘法运算符*重复元组
print(point)
point = tuple([1, 2]) # 将列表转换为元组
print(point)
point = tuple("Hello World")  # 原始字符串中的每个字符都是元组中的一项，包括空格
print(point)
point = (1, 2, 3)
print(point[0:2])
x, y, z = point # 解包元组
if 10 in point:
    print("exists")

# 交换变量
x = 10
y = 11
z = x
x = y
y = z
x, y = y, x # 与上面三行等价，赋值运算符右侧是一个元组，此处等价于x, y = (11, 10)，再解包元组，于是赋值x,y
print("x", x)
print("y", y)
a, b = 1, 2

# 数组array（仅在处理大量数字时使用）
# array()第一个参数是typecode，typecode是一个字符的字符串，确定数组中对象的类型
# "i"是signed int带正负号的整型变量
from array import array
numbers = array("i", [1, 2, 3])
numbers.append(4) # append、insert、pop、remove
# numbers[0] = 1.0 会报错，这里每个对象都应该是整数。数组中的每个对象都是相同类型的，类型是创建数组时使用typecode确定的

# 集合set（无序且不重复）
# 用花括号{}定义集合
numbers = [1, 1, 2, 3, 4]
first = set(numbers) # 删除重复项
print(first)
second = {1, 5}
second.add(6)
second.remove(6)
len(second)
# 数学运算
print(first | second) # 并集
print(first & second) # 交集
print(first - second) # 差集，一个集合减去交集
print(first ^ second) # 对称差集，并集减去交集
# 无序所以不能用索引
if 1 in first:
    print("yes")

# 字典dictionary（键值对的集合，也是集合）
# 将键映射到值，类似于现实生活中的电话簿
point = {"x": 1, "y": 2} # 键只能是不可变类型（字符串或数字），值可以是任何类型
point = dict(x=1, y=2)
point["x"] = 10 # 索引是key的名称
point["z"] = 20 # 添加项
print(point)
if "a" in point: # 检查key是否存在
    print(point["a"])
print(point.get("a")) # 如果key不存在，默认情况下返回None
print(point.get("a", 0)) # 第二个参数传递自定义的默认值
del point["x"]
print(point)
# 迭代字典
for key in point:
    print(key, point[key])
for x in point.items(): # 把键值对转换为元组
    print(x) # 每次迭代得到一个元组，元组中有键和值
for key, value in point.items():
    print(key, value)

# 字典推导式
# 语法：{key: value for item in iterable if condition}
# 列表推导式
values = []
for x in range(5):
    values.append(x * 2)
values = [x * 2 for x in range (5)] # 与上面三行代码等价
print(values)
# 没有元组推导式
# 集合推导式
values = {x * 2 for x in range(5)}
print(values)
# 字典推导式
values = {} # {}是空字典，不是空集合，创建空集合用set()
for x in range(5):
    values[x] = x * 2
print(values)
values = {x: x * 2 for x in range(5)}
print(values)

# 生成器generator（生成器对象可迭代，每次迭代生成一个新值，总共只生成一个值）
values = [x * 2 for x in range (100000)] # 如果数据集非常大，内存很大很低效
# for x in values:
#     print(x)
print("list:", getsizeof(values))
# 生成器表达式的语法： (expression for item in iterable if condition)
from sys import getsizeof
values = (x * 2 for x in range(100000))
# for x in values:
#     print(x) 返回结果和列表推导式一样
print(values)
print("generator:", getsizeof(values)) # 生成器对象的大小
# print(len(values))会报错，生成器对象没有长度

# 解包运算符（在任何可迭代对象中取出项）
numbers = [1, 2, 3]
print(numbers) # 返回列表，如果只想返回数字print(1, 2, 3)
print(1, 2, 3)
print(*numbers) # *是解包运算符，打开容器取出它的各个元素，并将它们作为任意参数传递给print函数
values = list(range(5))
print(values)
values = [*range(5), *"Hello"] # 解包运算符可以解包任何迭代，这里先解包range对象和字符串取出值，再把值放入list
print(values)
first = [1, 2]
second = [3]
values = [*first, "a", *second, *"Hello"] # 合并多个列表
print(values)
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1} # 解包字典并合并多个字典
print(combined) # 如果有多个相同的key，将使用最后一个值

# exercise：假设有一些文字，写代码找出重复最多的字符
sentence = "This is a common interview question"
# 需要知道每个字符重复的次数，应该用什么样的数据结构？字典，字典是键值对的集合，字符作为键，重复次数作为值
from pprint import pprint
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
print(char_frequency)
pprint(char_frequency, width=1) # width确定每行的字符数
# 下一步是按字符的频率对字典进行排序，但字典是集合，集合是无序的，只能对列表进行排序，所以字典转换为列表，取出字典的项，再把它们放列表中进行排序
# 字典.items()把键值对转换为元组
char_frequency_sorted =  sorted(char_frequency.items(), key=lambda kv:kv[1], reverse=True) # 排序依据是元组的第二项，kv是形参
print(char_frequency_sorted)
print(char_frequency_sorted[0])
