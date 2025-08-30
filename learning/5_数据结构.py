# 数据结构（列表list[]，元组tuple()，集合，字典dictionary）
from numpy.ma.core import append

# 列表的创建
# 用方括号[]定义列表，列表中的每个成分都可以是任意类型的
letters = ["a", "b", "c"] # 字符串列表，还有数字列表、布尔值列表
matrix = [[0, 1], [2, 3]] # 列表的列表，列表的每个成分本身都是一个列表（矩阵，二维列表）
zeros = [0] * 5 # 创建有5个0的列表，[0]是只有一个成分（0）的列表，用星号*重复列表中的成分
combined = zeros + letters # 用加号+连接多个列表
numbers = list(range(20)) # 创建从0到19的列表，list()函数需要可迭代对象，并将其转换为列表；range()函数返回range对象
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

# 元组
letters = ["a", "b", "c"]
for letter in letters: # for循环迭代列表
    print(letter)
# 获得每个成分的索引（enumerate()函数）
for letter in enumerate(letters): # enumerate()函数返回可迭代的enumerate对象；在每次迭代中，enumerate对象会返回一个含2项的元组（元组类似于列表，但是是只读的）
    print(letter) # 元组中的第一项是索引，第二项是该索引对应的成分
for letter in enumerate(letters):
    print(letter[0]) # 返回索引，letter是元组
    print(letter[0], letter[1]) # 解包元组，不简洁，letter[1]是每元组的第二项
# 解包元组
items = (0, "a")
index, letter = items
letters = ["a", "b", "c"]
for index, letter in enumerate(letters):
    print(index, letter)

# 向列表中添加新成分+删除现有成分
letters = ["a", "b", "c", "d", "e"]
# Add
# 在列表末尾添加成分
letters.append("f")
print(letters)
# 在特定位置添加成分
letters.insert(0, "-") # 列表开头
print(letters)
# Python中的一切都是对象，当函数是对象的一部分时，将该函数称为方法，该对象中的方法x.function
# Remove
# 删除列表末尾的成分
letters.pop() # 赋值再打印，会返回被删除的末尾成分
print(letters)
# 删除给定索引处的成分，只能删除一个成分
letters.pop(0)
print(letters)
# 删除某个成分但不知道它的索引
letters.remove("b") # 删除第一个"b"
print(letters)
# 通过索引删除成分，可以删除一个或多个成分
del letters[0:3]
print(letters)
# 删除列表中所有成分
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
def sort_item(item): # 定义函数用于排序，此处参数item代指列表中的成分——元组
    return item[1] # 返回价格用于排序
# 函数的作用是接受一个元组并返回它的价格
items.sort(key=sort_item) # key参数指定排序依据，sort的第一个参数不是key，所以必须明确指定
# sort_item：加括号sort_item()表示调用函数，()内需要填入参数否则报错，不加括号sort_item表示引用函数
# sort()排序时，会对每个成分调用sort_item()函数
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
# map()函数使得items列表中每个成分作为lambda函数的输入，此处lambda函数转换原始列表中的每个成分
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
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop() # 按下后退按钮，删除最后一项
print(last)
print(browsing_session)
print("redirect", browsing_session[-1]) # 重定向到之前的网站，即堆栈顶部的项
if not browsing_session: # 检查堆栈是否为空，not运算符应用于空列表的值为布尔值True
    print("disable")

# 队列queues（先进先出）

