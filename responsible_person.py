from person import Person


class ResponsiblePerson:
    def __init__(self, person: Person):
        self.person = person

    def check_if_drink(self)-> str:
        return self.person.drink() if self.person.age >= 18 else "Muito jovem"
    
    def check_if_drive(self) -> str:
        return self.person.drive() if self.person.age >= 16 else "Muito jovem"

    def check_if_drink_and_drive(self)-> str:
        if self.check_if_drink() == "drinking" and self.person.drive() == "driving":
            return self.person.drink_and_drive() + ", Morto"
        else:
            return "Se beber não dirija"

