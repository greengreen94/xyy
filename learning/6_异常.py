# 异常exception
# 异常是终止程序执行的一种错误
# example1
# numbers = [1, 2]
# print(numbers[3])
# example2
# age = int(input("Age: ")) # input()函数返回字符串，输入非数值a，ValueError

# 处理异常（防止程序崩溃）
try:
    age = int(input("Age: "))
except ValueError as ex: # 只处理ValueError异常，定义变量ex，变量ex包含有关异常的详细信息
    print("You didn't enter a valid age.") # python执行try块中的每一条语句，如果任何一条语句引发异常，except子句中的代码将被执行，如果没有任何异常，此代码不会执行
    print(ex)
    print(type(ex))
else: # 可选
    print("No exceptions were thrown.") # 如果try块代码没有异常，else块将会执行，类似于for,else
print("Execution continues.") # 正确处理异常，即使发生异常，此语句也会执行

# 处理不同类型的异常
try:
    age = int(input("Age: "))
    xfactor = 10 / age # 输入0
except ValueError:
    print("You didn't enter a valid age.")
except ZeroDivisionError:
    print("Age cannot be 0.")
else:
    print("No exceptions were thrown.")
try:
    age = int(input("Age: "))
    xfactor = 10 / age # 输入0
except (ValueError, ZeroDivisionError): # 两种异常输出相同信息，如果try块的任何一条语句出现与第一个except子句匹配的异常，其他except子句将被忽略
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")

# 释放
# 与外部资源（文件/网络连接/数据库连接等）合作，使用完资源需要释放它们
try:
    file = open("caogao.py") # 返回文件对象，获取open函数的返回值
    age = int(input("Age: "))
    xfactor = 10 / age
    # file.close() # 关闭文件对象，1：这里如果上面两行有异常，将会直接执行except子句，这行不会执行
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
    # file.close() # 2：只有有异常时才会执行，如果没有异常，将会执行else子句；3：重复
else:
    print("No exceptions were thrown.")
    # file.close() # 3：重复
finally: # 不管有没有异常，都会执行，所以用来释放外部资源
    file.close()

# with语句（自动释放外部资源）
try:
    with open("caogao.py") as file, open("another.txt") as target: # file是open函数返回的文件对象，打开文件使用with语句自动关闭；多个外部资源
        print("File opened.")
        # file.__enter__() # 点.后面是文件对象的成员
        # file.__exit__() # 当一个对象有这两种方法（进入和退出）时，那么该对象支持上下文管理协议，那么可以将该对象与with语句一起使用，自动调用exit方法释放外部资源
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")

# 引发异常raise exception（不要用）
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.") # 该函数引发异常，当实参无效时
    return 10 / age
try: # 处理异常
    calculate_xfactor(-1)
except ValueError as error:
    print(error)

# 引发异常的代价
from timeit import timeit # 计算代码执行时间
# 引发异常的代价
code1 = """ # 三引号创建多行字符串
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.") # 该函数引发异常，当实参无效时
    return 10 / age
try: # 处理异常
    calculate_xfactor(-1)
except ValueError as error:
    pass # 没有任何作用，用它是因为except块不能为空
"""
print("first code=", timeit(code1, number=10000)) # 执行代码10000次的时间
# 没有引发异常的代价
code2 = """ 
def calculate_xfactor(age):
    if age <= 0: # 思考if语句是否能够替代引发异常，引发异常是否真的有必要
        return None
    return 10 / age
xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""
print("second code=", timeit(code2, number=10000))
