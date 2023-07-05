# Classes

# keyword -> class

class Person:
    def __init__(self, *, first_name: str, last_name: str, final_age: int, skin_color: str):
        self.first_name = first_name
        self.last_name = last_name
        self.final_age = final_age
        self.skin_color = skin_color

    def __str__(self) -> str:
        return f"Person[first_name={self.first_name}, last_name={self.last_name}, final_age={self.final_age}, skin_color={self.skin_color}]"

    @property
    def get_fullname(self):
        return self.first_name + " " + self.last_name

    @property
    def get_age(self):
        return self.final_age

    def eat(self):
        print("I am eating, uuuhmmm...")

    def talk(self):
        print("I am talking plentyyyyy, my friends don't like it.")

    def walk(self):
        print(f"I am {self.get_fullname}, and I like walking.")
    


# Creating objects
akua = Person(first_name="Akua", last_name="Frimpong", final_age=89, skin_color="black")

print(akua.get_fullname)
print(akua.get_age)

akua.talk()
akua.eat()
akua.walk()
