#多态，即多种状态、形态，
#就是同一种行为对于不同的子类【对象】有不同的行为表现
#堕胎可以增加程序的灵活性和拓展性
#鸭子类型：不管你是什么对象，是duck对象也好，是dog对象也罢，只管对象实现who()方法就可。这就是鸭子类型，它根本不管你是什么对象，只要你有这个方法，有这个行为，表现得像鸭子，走起来像鸭子，游泳起来鸭子，叫起来也像鸭子，那么尽管你是一只会飞天的猪，也是称为鸭子类型。
def commonInvoke(obj):
    obj.say_what()

class People():#父类
    def say_what(self):
        print("我是labmam")
        pass
    pass

class Animal():#父类
    def say_what(self):
        print("我是一只动物")
        pass
    pass

class Dog(Animal):#子类
    def say_what(self):
        print("汪汪汪")
        pass
    pass

class Kiomo(People):#子类
    def say_what(self):
        print("我是凤凰院凶真")
        pass
    pass

class Kris(People):#子类
    def say_what(self):
        print("我是牧濑红莉栖")
        pass
    pass

class Dudulu(People):#子类
    def say_what(self):
        print("我是椎名真由理")
        pass
    pass

class Dalu(People):#子类
    def say_what(self):
        print("我是达鲁")
        pass
    pass


listObj=[Kiomo(),Kris(),Dudulu(),Dalu(),Dog()]#其中的Dog()只要有这个say_what()方法，有这个行为，表现得像鸭子，走起来像鸭子，游泳起来鸭子，叫起来也像鸭子，那么尽管你是一只会飞天的猪，也是称为鸭子类型。
for item in listObj:
    commonInvoke(item)