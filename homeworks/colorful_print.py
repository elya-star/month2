from blessed import Terminal
term = Terminal()
from homework_1 import Person
# print(term.red + "Apple" + term.normal)
# print(term.darkturquoise + "Orange" + term.normal)
# print(term.yellow + "Banana" + term.normal)

fruits_color = {
    "apple": term.red,
    "banana": term.green,
    "cherry": term.orange,
    "grape": term.blue,
    "mango": term.purple,
    "orange": term.cyan,
    "peach": term.pink,
}
for fruit, color in fruits_color.items():
    print(color + fruit + term.normal)

saadat = Person("saadat", "2006", "lox")
nelya = Person("nelya", "2007", "lox2")
print(term.cyan + saadat.name + term.normal)
print(term.green + saadat.birth_year + term.normal)
print(term.blue + saadat.occupation + term.normal)
print(term.yellow + str(saadat.higher_education) + term.normal)
print()

print(term.cyan + nelya.name + term.normal)
print(term.green + nelya.birth_year + term.normal)
print(term.blue + nelya.occupation + term.normal)
print(term.yellow + str(nelya.higher_education) + term.normal)
print()

saadat.introduce()
nelya.introduce()