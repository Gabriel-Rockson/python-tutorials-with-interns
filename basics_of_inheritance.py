class Animal:
    def __init__(self, name: str, number_of_legs: int, has_fur: bool, number_of_eyes: int, has_tail: bool, number_of_horns: int) -> None:
        self.name = name
        self.number_of_legs = number_of_legs
        self.has_fur = has_fur
        self.number_of_eyes = number_of_eyes
        self.has_tail = has_tail
        self.number_of_horns = number_of_horns

    def walk(self):
        print("I am walking")

    def make_sound(self):
        print("I am making a sound")

    def eat(self):
        print("I am eating")

    def is_alien(self) -> bool:
        return True if self.number_of_eyes > 2 or self.number_of_eyes == 0 else False

    def __str__(self) -> str:
        return f"{self.__class__.__name__}[name={self.name}, number_of_legs={self.number_of_legs}, has_fur={self.has_fur}, number_of_eyes={self.number_of_eyes}, has_tail={self.has_tail}, number_of_horns={self.number_of_horns}]"

class Cat(Animal):

    def __init__(self, name: str):
        number_of_legs = 4
        number_of_eyes = 2
        has_fur = True
        has_tail = True
        number_of_horns = 0
        super().__init__(name, number_of_legs, has_fur, number_of_eyes, has_tail, number_of_horns)

    def make_sound(self):
        print("Meow meow ...")
        super().make_sound()


class Goat(Animal):
    def __init__(self):
        name = "No Name"
        number_of_legs = 4
        has_fur = True
        number_of_eyes = 2
        has_tail = True
        number_of_horns = 2
        super().__init__(name, number_of_legs, has_fur, number_of_eyes, has_tail, number_of_horns)

class Human(Animal):
    def __init__(self, name: str):
        number_of_legs = 2
        has_fur = False
        number_of_eyes = 2
        has_tail = False
        number_of_horns = 0
        super().__init__(name, number_of_legs, has_fur, number_of_eyes, has_tail, number_of_horns)

class Dog(Animal):
    def __init__(self, name: str) -> None:
        self.name = name

    def make_sound(self):
        print("BARK BARK BARK !!!")

cat = Cat("V Cat")
goat = Goat()
akua = Human("Akua Frimpong")

print(cat)
print(goat)
print(akua)
