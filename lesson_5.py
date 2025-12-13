class Animal:
    def move(self):
        print("двигается")
class Swimming(Animal):
    def move(self):
        print("плавает")

class Flying(Animal):
    def move(self):
        print("летает")

class Duck(Swimming, Flying):
    def move(self):
        print("летает и плавает")
        super().move()


duck = Duck()
duck.move()
# MRO = method resolution order
# порядок поиска методов
print(Duck.mro())