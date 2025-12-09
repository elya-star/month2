class Person:
    def __init__(self, name, birth_year, occupation):
        self.name = name
        self.birth_year = birth_year
        self.occupation = occupation
        self.higher_education = False
    def introduce(self):
        print(f"My name is {self.name}, I born in {self.birth_year}, my occupation is {self.occupation}, my higher education is {self.higher_education}")

saadat = Person("Saadat", "2006", "lox")
print(saadat.name)
print(saadat.birth_year)
print(saadat.occupation)
print(saadat.higher_education)

nelya = Person("Nelya", "2007", "lox2")
print(nelya.name)
print(nelya.birth_year)
print(nelya.occupation)
print(nelya.higher_education)

saadat.introduce()
print(saadat.introduce)
nelya.introduce()
print(nelya.introduce)