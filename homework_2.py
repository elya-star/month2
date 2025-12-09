class Person:
    def __init__(self, name, birth_year, occupation):
        self.name = name
        self.birth_year = birth_year
        self.occupation = occupation
        self.higher_education = False
    def introduce(self):
        print(f"Меня зовут {self.name}, Я родилась в {self.birth_year} году, работаю: {self.occupation}, my higher education is {self.higher_education}")

class Classmate(Person):
    def __init__(self, group_name, name, birth_year, occupation):
        self.group_name = group_name
        self.name = name
        self.birth_year = birth_year
        self.occupation = occupation
    def introduce(self):
        print(f"Привет, меня зовут {self.name},родился в {self.birth_year}, состою в группе {self.group_name}, работаю {self.occupation}")
class Friend(Person):
    def __init__(self, hobby, name, birth_year, occupation):
        self.hobby = hobby
        self.name = name
        self.birth_year = birth_year
        self.occupation = occupation
    def introduce(self):
        print(f"Привет, меня зовут {self.name}, родилась в {self.birth_year},работаю {self.occupation} и у меня есть хобби: {self.hobby}")

classmate1 = Classmate("P1", "Александра", 2007, "моделью")
classmate1.introduce()
classmate2 = Classmate("P2", "Кими", 2006, "профессиональным гонщиком в F1 ")
classmate2.introduce()

bro1 = Friend("рисовать", "Кими", 2006, "профессиональным гонщиком в F1")
bro1.introduce()
bro2 = Friend("создавать парфюм", "Жанна", 2007, "дизайнером")
bro2.introduce()

# доп задание 1:
classmate3 = Classmate("P1", "Володя", 2005, "учителем")
bro3 = Friend("вязать крючком", "Эля", 2007, "няней")
person = Person("Анна Георгиевна", 1980, "бухгалтером")
people = [classmate3, bro3, person]
for person in people:
    person.introduce()

# доп задание 2:
class BestFriend(Friend):
    def __init__(self, hobby, name, birth_year, occupation, shared_memory):
        super().__init__(hobby, name, birth_year, occupation)
        self.shared_memory = shared_memory
    def introduce(self):
        super().introduce()
        print(f"люблю {self.shared_memory}")

bestbro = BestFriend("смотреть фильмы или сериалы", "Саадат", 2006,"беззработной тюленью", "ходить с тобой в кино")
bestbro.introduce()