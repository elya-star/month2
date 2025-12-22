class Car:
    # инициализатор или конструктор
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.fined = False
    def drive_to(self, destination):
        print(f"Car {self.model} Driving to", destination)
    def change_color(self, new_color):
        self.color = new_color
        print(f"Car {self.model} Changing color to {new_color}")
car_honda = Car(color="red", model="MClaren")
car_subaru = Car(color="silver", model="Mercedes Benz")
if __name__ == "__main__":
    print(car_honda)
    print(car_subaru)
    car_honda.fined = True
    print(car_honda.fined)
    print(car_honda.color)
    print(car_honda.model)
    print(car_subaru.color)
    print(car_subaru.model)
    car_honda.color = "green"
    print(car_honda.color)
    car_honda.year = 2020
    print(car_honda.year)
    car_subaru.drive_to("Bishkek")
    car_subaru.change_color("blue")

class Computer:
    def __init__(self, screen_diagonal, model):
        self.model = model
        self.screen_diagonal = screen_diagonal
        self.state = "off"

    def turn_on(self):
        if self.state == "off":
            print(f"Computer {self.model} is turned on")

    def turn_off(self):
        if self.state == "on":
            print(f"Computer {self.model} is turned off")


computer_asus_zenbook = Computer(screen_diagonal=16, model="Asus Zenbook")
computer_asus_vivobook = Computer(screen_diagonal=16, model="Asus Vivobook")
computer_lenovo_yoga = Computer(screen_diagonal=14, model="Lenovo Yoga")
if __name__ == "__main__":
    print(computer_lenovo_yoga.model, computer_lenovo_yoga.screen_diagonal)
    print(computer_asus_zenbook.model, computer_asus_zenbook.screen_diagonal)

    computer_asus_vivobook.turn_on()
    computer_asus_vivobook.turn_off()
    computer_asus_vivobook.turn_off()
