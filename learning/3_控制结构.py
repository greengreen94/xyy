# 比较运算符
# 数值
print(10 >= 3) # 布尔表达式（产生布尔值的表达式）
print(10 == 10)
print(10 == "10")
print(10 != "10")
# 字符串（字符串比较大小，按ASCII比较第一个字符大小，一样就比较第二个字符大小，不一样就出结果，依此类推）
print("bag" > "apple") # 按字母表排序，bag在apple后面
print("bag" == "BAG")
# 每个字母都有数字表示
print(ord("b")) # 98，字母b的数字表示
print(ord("B")) # 66，b的ASCII大于B，小写字母和大写字母具有不同的数字表示

# 分支结构
# 单分支结构：if语句
temperature = 35
if temperature > 30: # 条件是布尔表达式
    print("It's warm")
    print("Drink water") # 记得一定要缩进，缩进的语句才是if条件为真返回的语句
print("Done") # 表示if语句的结束，没有缩进，无论条件是真是假都会执行

# 二分支结构：if-else语句
# 多分支结构：if-elif-else语句
# 1、多条件
temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20: # elif: else if
    print("It's nice")
else:
    print("It's cold")
print("Done")

# 2、二分支&给变量赋值
age = 22
# if age >= 18:
#     message = "Eligible"
# else:
#     message = "Not eligible"
message = "Eligible" if age >= 18 else "Not eligible" # 与上面四行代码等价，当给变量赋值时
print(message)

# 3、and,or,not逻辑运算符（not > and > or）
high_income = False
good_credit = True
student = True
# and
if high_income and good_credit: # high_income已经是布尔值，不需要写成high_income == True
    print("Eligible")
else:
    print("Not eligible")
# or
if high_income or good_credit:
    print("Eligible")
else:
    print("Not eligible")
# not
if not student: # 条件是假的，所以print语句不执行，条件为真时才执行
    print("Eligible")
else:
    print("Not eligible")
# and,or,not
if (high_income or good_credit) and not student: # 条件：收入高或信用好，不是学生，注意这里一定要括号
    print("Eligible")
else:
    print("Not eligible")

# 4、链式比较运算符
age = 22
if 18 <= age < 65: # 等价于if age >= 18 and age < 65:
    print("Eligible")

# 循环结构
# for循环（遍历循环，迭代可迭代的对象）
# 可迭代对象：range、字符串、列表、自定义
# 1、for语句
for number in range(3): # number分别是0、1、2，只有1个参数，从0开始到该参数前结束
    print("Attempt", number + 1, (number + 1) * ".")
for number in range(1, 4): # number分别是1、2、3，从第1个参数开始，到第2个参数前结束，左闭右开
    print("Attempt", number, number * ".")
for number in range(1, 10, 2): # 第3个参数是step步长
    print("Attempt", number, number * ".")

# 2、break
# 满足某个条件就跳出循环
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break

# 3、for,else语句
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break # 因为if条件为假，没有break，所以先for循环0、1、2这3次再else
else: # 这个else是for,else语句，不是if,else语句。如果for循环没有提前终止，else语句一定会执行，如果break了，else就不会执行
    print("Attempted 3 times and failed")

# 4、嵌套循环
for x in range(5): # 外循环
    for y in range(3): # 内循环
        print(f"({x}, {y})")

# 5、可迭代对象
print(type(5))
print(type(range(5))) # range：数据的复杂类型之一，可迭代
for x in range(3):
    print(x)
for x in "Python": # 字符串也可迭代
    print(x)
for x in [1, 2, 3, 4]: # 列表：数据的复杂类型之一，这里是数值列表，也可迭代。用方括号创建列表
    print(x)
# for item in shopping_cart: # shopping_cart是创建的可迭代的自定义对象
#     print(item)

# while循环（无限循环，评估条件，重复任务）
# 1、while语句
number = 100
while number > 0:
    print(number)
    number //= 2 # number = number // 2

# 2、while循环&用户输入
command = ""
while command != "quit": # 只有输入小写quit才会终止
    command = input(">") # 从用户那里获得输入
    print("ECHO1", command) # 有空格

# 3、while循环&用户输入
command = ""
while command.lower() != "quit": # 只要输入quit无论大小写都会终止
    command = input(">")
    print("ECHO2", command)

# 4、while&break
# 无限循环及其终止，和上面代码等价
while True:
    command = input(">")
    print("ECHO3", command)
    if command.lower() == "quit":
        break

# exercise：显示1到10之间（左闭右开不包括10）的偶数，并打印偶数个数
count = 0
for x in range(1, 10):
    if x % 2 == 0:
        print(x)
        count += 1
print(f"We have {count} even numbers")