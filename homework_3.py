class Person:
    def __init__(self, name, birth_year, occupation, higher_education: bool = False):
        self.name = name
        self.birth_year = birth_year
        self.__occupation = occupation
        self.__higher_education = higher_education
    def introduce(self):
        education_status = "У меня есть высшее образование" if self.higher_education else "У меня нет высшего образования"
        print(f"Меня зовут {self.name}, Я родилась в {self.birth_year} году, работаю: {self.occupation}, my higher education is {education_status}")
    @property
    def occupation(self):
        return self.__occupation
    @property
    def higher_education(self):
        return self.__higher_education
    @higher_education.setter
    def higher_education(self, has_higher_education: bool):
        self.__higher_education = has_higher_education

    @occupation.setter
    def occupation(self, occupation):
        self.__occupation = occupation

class Classmate(Person):
    def __init__(self, group_name, name, birth_year, occupation, higher_education: bool = False ):
        super().__init__(name, birth_year, occupation, higher_education)
        self.group_name = group_name


    def introduce(self):
        education_status = "У меня есть высшее образование" if self.higher_education else "У меня нет высшего образования"
        print(f"Привет, меня зовут {self.name},родился в {self.birth_year}, состою в группе {self.group_name}, работаю {self.occupation}. {education_status}")
class Friend(Person):
    def __init__(self, hobby, name, birth_year, occupation, higher_education: bool = False):
        super().__init__(name, birth_year, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        education_status = "У меня есть высшее образование" if self.higher_education else "У меня нет высшего образования"
        print(f"Привет, меня зовут {self.name}, родилась в {self.birth_year},работаю {self.occupation} и у меня есть хобби: {self.hobby}. {education_status} ")

classmate1 = Classmate("P1", "Александра", 2007, "моделью", True)
classmate1.introduce()
classmate2 = Classmate("P2", "Кими", 2006, "профессиональным гонщиком в F1 ", False)
classmate2.introduce()

bro1 = Friend("рисовать", "Кими", 2006, "профессиональным гонщиком в F1", False)
bro1.introduce()
bro2 = Friend("создавать парфюм", "Жанна", 2007, "дизайнером", True)
bro2.introduce()