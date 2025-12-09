class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def make_sound(self):
        return "Звуки животных"

class Dog(Animal):
    def make_sound(self):
        return "гав-гав"
class Cat(Animal):
    def make_sound(self):
        return "мур-мур"

bobik = Dog("bobik", 2)
shket = Cat("shket", 3)

print(f"{bobik.get_name()}, {bobik.get_age()}")
print(f"{shket.get_name()}, {shket.get_age()}")

print(f"{bobik.get_name()} говорит: {bobik.make_sound()}")
print(f"{shket.get_name()} говорит: {shket.make_sound()}")

bobik.set_name("Sharik")
bobik.set_age(1.5)
shket.set_name("Peter")
shket.set_age(2.5)

print(f"{bobik.get_name()}, {bobik.get_age()}")
print(f"{shket.get_name()}, {shket.get_age()}")

