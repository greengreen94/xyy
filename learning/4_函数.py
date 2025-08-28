# 函数的定义与调用
def greet(): # define，greet为函数名
    print("Hi")
    print("Welcome")
greet()

# 函数的参数传递
def greet(first_name, last_name): # 形参parameters：为函数定义的输入
    print(f"Hi {first_name} {last_name}")
    print("Welcome")
greet("Hua", "Li") # 实参arguments：形参的实际值
# greet("Hua") # 默认情况下，为函数定义的所有参数都是必需的，这里少了一个参数会报错

# 函数类型
# 类型1：执行任务的函数
# 类型2：（计算并）返回值的函数
def greet(name): # 类型1
    print(f"Hi {name}")
def get_greeting(name): # 类型2
    return f"Hi {name}"
message = get_greeting("Feng")
print(message) # 函数类型2可以在终端上打印
# file = open("content.txt", "w") # 也可以使用open函数将其写入文件
# file.write(message)
greet("Feng")
print(greet("Feng")) # 默认情况下，所有函数返回None值，即使没有return语句（None是表示没有值的对象）
# 也就是说，函数类型1没有return语句但会返回None值，只不过None没有被打印出来，这里调用print就会被打印出来；函数类型2指定了return值，所以不会返回None值

# 设置可选参数（可选参数在必需参数之后）
def increment(number, by): # 使一个数字递增一个给定的值
    return number + by
print(increment(2, 1))
print(increment(2, by=1))
# by参数可选
def increment(number, by=1): # by参数默认值为1
    return number + by
print(increment(2)) # 使用默认值1
print(increment(2, 5)) # 使用指定值5

# 设置可变数量参数（星号*）
def multiply(x, y):
    return x * y
print(multiply(2, 3))
# multiply(2, 3, 4, 5)报错
# 元组，星号*
def multiply(*numbers): # 在参数前加星号*时，获得所有任意参数，并将它们打包到一个元组中
    print(numbers) # 用括号()创建元组，元组是对象的集合，不能修改这个集合（用方括号[]创建列表）
multiply(2, 3, 4, 5) # 传递任意参数
# 元组可迭代
def multiply(*numbers):
    for number in numbers:
        print(number)
multiply(2, 3, 4, 5)
# 计算所有参数的乘积
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
        # return total # for循环遇见return会直接返回一个值并结束循环，所以返回2
    return total # 注意缩进，不是for循环的一部分
print(multiply(2, 3, 4, 5))

# 字典，双星号**
def save_user(**user): # 保存用户的信息
    print(user)
save_user(id=1, name="John", age=22) # 传递任意关键字参数name=value
# 字典：花括号。多个键值对（键冒号，值逗号）
def save_user(**user):
    print(user["id"]) # 这里id是钥匙的名称，返回钥匙的值
save_user(id=1, name="John", age=22)

# 局部local变量与全局global变量（scope作用域：变量的代码区域）
# 局部变量（name和message变量的作用域是greet函数）
def greet(name):
    message = "a"
def send_email(name):
    message = "b"
# print(name) # 报错，没有定义name变量
# print(message) # 报错，没有定义message变量
# Python解释器分配内存并让name和message变量引用这些内存位置，执行完greet函数，这些变量在其他任何地方都没有使用，被收集为垃圾，函数运行结束Python解释器将回收内存
# 全局变量（message变量的作用域是这个文件）
# 少用，创建带有参数和局部变量的函数
message = "a"
def greet(name):
    message = "b" # 为message变量分配新值
greet("Feng")
print(message) # 输出结果a。默认情况下将message="b"的message变量视为局部变量，即使它与message="a"的message全局变量同名。因此这两个变量是分开的
# 下面方法展示了如何在函数中修改message全局变量的值，但避免使用这个糟糕做法
message = "a"
def greet(name):
    global message # greet函数使用message全局变量，不会定义局部变量
    message = "b"
greet("Feng")
print(message)

# 如何发现和修复程序中的bug
# 调试
# 快捷键
# 光标直接移动到行尾：End；行首：Home
# 光标移动到文件开头：Ctrl+Home；文件末尾：Ctrl+End
# 复制一行或多行：选中再按Shift+Alt+向下箭头
# 注释：选中再按Ctrl+?

# Fizz Buzz算法
# 如果input可以被3整除，返回Fizz；如果input可以被5整除，返回Buzz；如果input可以被3和5整除，返回FizzBuzz；如果input不能被3或5整除，返回input
def fizz_buzz(input):
    if input % 3 == 0:
        result = "Fizz"
    else:
        result = "Buzz"
    return result
# 改进
def fizz_buzz(input):
    if input % 3 == 0:
        return "Fizz"
    else: # 当有if语句，在if中返回一个值时，不需要写else（原因见下面）
        return "Buzz"
# 再改进
def fizz_buzz(input):
    if input % 3 == 0:
        return "Fizz"
    return "Buzz"

def fizz_buzz(input): # 注意以下顺序
    if (input % 3 == 0) and (input % 5 == 0): # 这一句放最前面，加上括号更易读
        return "FizzBuzz" # 函数在触发第一个return时，会直接跳出当前函数，直接终止不会执行后面的return
    if input % 3 == 0: # 不需要elif和else
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input
print(fizz_buzz(3))
print(fizz_buzz(10))
print(fizz_buzz(15))
print(fizz_buzz(4))
print(fizz_buzz(0))