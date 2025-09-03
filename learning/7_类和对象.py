# 类Classes和对象
# numbers = [1, 2]
# numbers. 点表示法访问函数，或者说访问列表对象中的方法
x = 1
print(type(x)) # 返回<class 'int'>，Python中有个名为int的类创建整数
# Python中的每个对象都是使用类创建的
# 类：创建该类型对象的蓝图或模板，定义了对象所共有的属性（数据）和方法（函数）。eg：人类
# 对象：类的实例。eg：约翰、玛丽、杰克
# 比喻：想象一下汽车设计图就是一个类，而根据这张设计图制造出来的每一辆具体的汽车（比如你的车、我的车）就是对象或实例

# 创建自定义类
class Point: # 冒号以下是块，块中定义与Point相关的函数
# 类的命名规则：每个单词的首字母大写，不用下划线分隔，eg：MyPoint，变量和函数的命名规则：小写字母，下划线分隔多个单词
    def draw(self): # 绘制点的函数，类中的所有函数至少有一个参数，通常是self
    # 创建的每个Point对象都有draw这个方法
        print("draw")
point = Point() # point是Point类的对象
# point. # 使用点运算符可以看到draw方法，还有一堆没有定义的其他方法（继承）
print(type(point)) # 返回<class '__main__.Point'>，main是模块名称
print(isinstance(point, Point))
print(isinstance(point, int))
# isinstance(object, class)：isinstance()函数用于判断一个对象是否属于某个类（是否是某个类的实例），
# 或者是否属于由多个类组成的元组中的某一个，返回布尔值：True或False

# 构造方法/函数Constructors：__init__（魔术方法Magic Methods：用双下划线__包围的特殊方法）
# 创建Point对象时，想设置x和y的初始值，eg：Point(1, 2)
# __init__是一个初始化方法，在创建新对象时自动调用，用于设置对象的初始状态（即给属性赋初值）
class Point:
    def __init__(self, x, y): # 给Point对象设置初始值
    # 类中定义的所有方法至少有一个参数，通常是self，这里可选地添加用于初始化Point对象的任何附加参数
    # self参数是对当前实例/对象的引用，必须是任何实例方法的第一个参数
        self.x = x # 定义属性x，y，可以设置为默认值比如0，这里设置为实参x。此处第一个x是属性，第二个x是实参
        self.y = y
        # 对象也有属性，属性是包含关于该对象的数据的变量
        # 类或对象将数据和与该数据相关的函数捆绑到一个单元中
        # eg：人，属性：眼睛颜色、身高、体重等，函数：走路、说话等
    def draw(self): # self参数是对当前实例/对象的引用，所以可以读取x值和y值（当前对象的属性）并打印
        print(f"Point ({self.x}, {self.y})")
point = Point(1, 2) # 此处调用Point类，Python将在内存中创建一个Point对象，并将self设置为引用那个Point对象
# point. # 使用点运算符可以看到该对象的所有方法和属性
print(point.x)
point.draw() # 调用对象的方法时，不必为self参数提供值，python会默认这样做（给self参数提供值对象）
# point.draw(point) # 可以传递Point对象point作为对当前对象的引用（self），但没必要

# 类属性vs实例属性Class vs Instance Attributes
# 类属性：在类内部，但在任何方法之外；该类的所有实例/对象共享类属性；可以通过类引用或对象引用（ClassName.attr或instance.attr）读取
# 实例属性：通常在__init__方法内部，使用self.；每个实例都拥有自己的副本，互不影响；通过instance.attr读取
# 类只有类属性，对象既有实例属性又有类属性
class Point:
    default_color = "red" # 定义类属性（在类级别定义的属性），在类的所有实例中都是相同的，eg：所有人类都有两只眼睛和两只耳朵
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        print(f"Point ({self.x}, {self.y})")
point = Point(1, 2)
# 可以在创建Point对象后定义实例属性，因为对象是动态的，也就是说不必在构造函数中定义所有实例属性，可以在后面定义
point.z = 10 # x,y,z是实例属性，属于Point实例或Point对象，因此每个Point对象对实例属性可以有不同的值
print(point.default_color) # 对象引用访问类属性
print(Point.default_color) # 类引用访问类属性
point.draw()
another = Point(3, 4)
print(another.default_color)
another.draw() # 可以看到两个Point对象完全独立，每个Point对象有自己的实例属性，eg：约翰和玛丽有不同的眼睛颜色
Point.default_color = "yellow" # 注意此处使用的是类引用，类的所有实例共享类属性，如果改变类属性的值，更改对该类的所有对象都可见
print(point.default_color)
print(Point.default_color)
print(another.default_color) # 所有实例的类属性都被更改

# 类方法vs实例方法Class vs Instance Methods
# 创建初始值为（0,0）的Point对象很简单，但有时初始化对象（0,0,1,"a"）可能很复杂，可能还需要在几个地方重复此操作
# 这样的话，代替传递复杂初始值创建对象，定义一个工厂方法factory method，返回具有复杂初始值的对象
# 通过这种方式，将创建对象的复杂性转移到工厂方法中
# 工厂方法：专门负责创建对象的函数或方法。不直接使用ClassName()来创建对象，而是通过调用工厂方法来创建
# 类方法：有装饰器@classmethod；第一个参数是cls类引用；Class.method()或instance.method()调用；
# 只能通过cls参数访问类级别的属性和方法，不能直接访问任何实例的属性或方法；因为在调用类方法时，可能根本没有任何实例被创建出来。既然没有实例，自然就无法访问属于某个特定实例的属性
# 实例方法：无装饰器；第一个参数是self实例引用；instance.method()调用；可以通过self访问一切——它自己的实例属性、类属性、其他实例方法、其他类方法
class Point:
    def __init__(self, x, y): # 实例方法
        self.x = x
        self.y = y
    @classmethod # 类方法的装饰器
    def zero(cls): # 类方法，在类级别定义的方法，不需要现有的对象来引用
    # 定义类方法的第一个参数是cls，cls（class的简称）参数是对类本身的引用，因此不是在处理Point对象或Point实例
    # zero方法用于创建初始值为（0,0）的Point对象
        return cls(0, 0) # 其实就是Point(0, 0)，区别是运行时调用zero方法时使用cls，将自动传递对Point类的引用至zero方法
    def draw(self): # 实例方法
        print(f"Point ({self.x}, {self.y})")
point = Point(0, 0)
point = Point.zero() # 注意此处使用的是类引用，zero方法是工厂方法，返回初始值为（0,0）的Point对象
point.draw() # 使用Point类的实例调用实例方法，使用实例方法需要现有的对象来引用
# 此处point.draw()处理一个特定的Point对象，因此draw方法被称为实例方法（实例方法处理特定的实例/Point对象）
# 一个绝佳的类比：汽车与设计图
# 类 (Class) = 汽车设计图
# 类属性 (class_attr) = 设计图上的品牌标志（所有车都一样）
# 实例 (obj) = 根据设计图制造出来的一辆具体的汽车
# 实例属性 (instance_attr) = 这辆车的具体车牌号（每辆车都不同）
# 实例方法 = 这辆车的功能，如drive()。要开车，你必须有一辆具体的车（实例）。开车时，你既知道自己的车牌号（实例属性），也能看到车上的品牌标志（类属性）
# 类方法 = 设计图上的一个注释，比如“年产量估算”。你只需要看设计图（类）就能知道这个信息，不需要真的造一辆车出来。你无法通过设计图知道某辆具体车的车牌号

# 魔术方法Magic Methods（用双下划线__包围的特殊方法）
# __init__: 初始化
# __str__: 定义str(obj)和print(obj)的友好输出
# __repr__: 定义repr(obj)的明确、无歧义的输出，通常用于调试
# __len__: 定义len(obj)的行为
# __getitem__, __setitem__: 定义索引操作obj[key]和赋值obj[key]=value
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def _str_(self):
        return f"({self.x}, {self.y})"
    def draw(self):
        print(f"Point ({self.x}, {self.y})")
point = Point(1, 2)
print(str(point))

# 比较对象Comparing Objects
# __eq__(self, other): 定义==行为
# __ne__(self, other): 定义!=行为（通常自动从__eq__派生）
# __lt__(self, other): 定义<行为
# __le__(self, other): 定义<=行为
# __gt__(self, other): 定义>行为
# __ge__(self, other): 定义>=行为


# 执行算术运算Performing Arithmetic Operations
# __add__(self, other): +
# __sub__(self, other): -
# __mul__(self, other): *
# __truediv__(self, other): /



# 创建自定义容器Making Custom Containers
# 通过实现容器协议的方法（如__getitem__,__setitem__,__delitem__,__len__,__iter__,__contains__），你可以创建类似列表、字典的自定义容器


# 私有成员Private Members
# Python 没有真正的“私有”变量。它通过名称改写（Name Mangling） 来实现一种伪私有机制
# 在属性或方法名前加双下划线 __（但末尾不能也有双下划线），Python 会自动将其名称改写为 _ClassName__membername
# 这主要是为了避免子类意外重写父类的私有方法和属性
# 单下划线 _ 是一种命名约定，表示“这是一个内部使用的属性/方法，请勿随意访问”（Protected）。这更像是一种提示，而不是强制限制


