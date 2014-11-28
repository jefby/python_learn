__author__ = 'jefby'
#coding=utf-8
'''
class Person:
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
    def greet(self):
        print "Hello,world! I'm %s." % self.name

#继承自类Person
class Man(Person):
    def greet(self):#覆盖基类Person中的定义greet
        print "Hello,world!I'm a man,my name is %s." % self.name
#继承自基类Person
class Woman(Person):
    def greet(self):
        print "Hello,world!I'm a woman,my name is %s." % self.name
foo = Person()
bar = Person()
foo.setName('Luke Skywalker')
bar.setName('Anakin Skywalker')

foo.greet()
bar.greet()

foo = Man()
foo.setName('Luke Skywalker')
foo.greet()
print foo.name
print foo.__doc__

bar = Woman()
bar.setName('Anakin Skywalker')
bar.greet()

'''

__metaclass__ = type #super函数只在新式类中起作用
class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print 'Aaaah....'
            self.hungry = False
        else:
            print 'No,thanks!'
class SongBird(Bird):
    def __init__(self):
#        Bird.__init__(self)
        super(SongBird,self).__init__()
        self.sound = 'Squawk'
    def sing(self):
        print self.sound


b = Bird()
b.eat()
b.eat()

sb = SongBird()
sb.sing()
sb.eat()
sb.eat()

__metaclass__ = type
class MyClass:
    @staticmethod
    def smeth():
        print 'This is a static method'
    @classmethod
    def cmeth(cls):
        print 'This is a class method of',cls
MyClass.smeth()
MyClass.cmeth()


