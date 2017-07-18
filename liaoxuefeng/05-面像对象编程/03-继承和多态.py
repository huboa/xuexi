
#编写了一个名为Animal的class，有一个run()方法可以直接打印
class Animal(object):
    def run(self): print('Animal is running...')
#当我们需要编写Dog和Cat类时，就可以直接从Animal类继承：
class Dog(Animal):
    pass
class Cat(Animal):
    pass

###Dog和Cat作为它的子类，什么事也没干，就自动拥有了run()方法
dog = Dog()
dog.run()
cat = Cat()
cat.run()

####子类包含同样方法的时候就覆盖父类方法
class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Eating meat...')

####要理解多态的好处，我们还需要再编写一个函数，这个函数接受一个Animal类型的变量
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')
run_twice(Tortoise())