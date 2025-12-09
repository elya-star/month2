class Person:
    def __init__(self, name, birth_year, occupation):
        self.name = name
        self.birth_year = birth_year
        self.occupation = occupation
        self.higher_education = False
    def introduce(self):
        print(f"My name is {self.name}, I born in {self.birth_year}, my occupation is {self.occupation}, my higher education is {self.higher_education}")

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