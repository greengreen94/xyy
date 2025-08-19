# 变量（将数据存储在计算机内存中）
# 数据的基本类型：数字、布尔值True/False和字符串（区分大小写）

# 字符串类型
course = "Python Programming"
print(len(course)) # len()字符串的长度，不局限于字符串，长度18，空格也算
# []访问字符串中的特定字符
print(course[0]) # 第1个字符的索引为0
print(course[-1]) # 字符串末尾的第1个字符
print(course[0:3]) # 前3个字符，012，不包括结束索引处的字符3，左闭右开
print(course[0:])
print(course[:3])
print(course[:])
print(course[1:-1])

# \转义字符
# 转义序列：\"表示"，\'表示'，\\表示\，\n表示换行
course = "Python \n Programming"
print(course)

# 格式化字符串（常量）
first = "Hua"
last = "Li"
full = first + " " + last
print(full)
full = f"{first} {last}" # f可大写可小写，{}为字段，f后跟着引号
print(full)
full = f"{len(first)} {2 + 2}"
print(full)

# 字符串函数
course = "Python Programming"
# 点表示法访问函数
print(course.upper()) # 全部大写
print(course.lower()) # 全部小写
course = "python programming"
print(course.title()) # 每个单词的第一个字母大写
course = "    python programming  "
print(course.strip()) # 移除字符串开头和结尾的空白
print(course.rstrip()) # 移除字符串结尾的空白，lstrip移除字符串开头的空白
course = "python programming"
print(course.find("pro")) # 返回字符串中字符序列的索引，从0开始
print(course.find("Pro")) # 注意大小写，输出结果-1意味着在原始字符串中找不到此字符串
print(course.replace("py", "j")) # 替换
print("pro" in course) # 查看字符串是否包含字符序列，返回布尔值
print("green" not in course)

# 数字类型（整数、浮点数、复数）
x = 1
x = 1.1
x = 1 + 2j # a + bi
# 算术运算符
# 加+，减-，乘*，除/
# 除法的整数//，除法的余数、模%，次方**
# 增广赋值运算符+=
x = 10
x = x + 3
x += 3 # 与上式等价

# 数值函数
print(round(2.8)) # 四舍五入
print(abs(-2.8)) # 绝对值
import math # math模块
print(math.ceil(2.3)) # 向上取整
print(math.floor(2.3)) # 向下取整

# 类型转换函数
# int(x) # 转换为整数
# float(x) # 转换为浮点数
# bool(x) # 转换为布尔值
# str(x) # 转换为字符串
x = input("x:") # input()从用户那里获得输入作为参数，等待用户在终端输入内容，""返回字符串，x:是标签是提示符会在终端显示
print(type(x))
# y = x + 1 # "1" + 1，字符串不能与数字相加，会报错
y = int(x) + 1 # 将字符串转换为数字
print(f"x: {x}, y:{y}")

# 布尔值True/False（注意大小写）
# 布尔假：""空字符串、0、None，除了这些其他都是布尔真
print(bool(0)) # bool(非零值)均为True
print(bool(None))
print(bool(""))
print(bool("False")) # 非空字符串均为True