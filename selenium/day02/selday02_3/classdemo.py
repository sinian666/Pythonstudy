class Person():
    #属性
    name = '张三'
    age = 20
    gender = '女'
    #方法
    def eat(self):
        print("吃饭")
        print(self.name) #调用属性
        self.native = "北京"
    def sleep(self):
        print("睡觉")
class Student(Person):
    score = 90
    sno = 8
    def study(self):
        print("学习")

p = Person()
p.eat()
print(p.name , p.gender , p.age ,p.native)
p.sleep()
s = Student()
print(s.name , s.gender , s.age , s.sno , s.score)
s.sleep()
s.eat()
s.study()
print(s.native)
