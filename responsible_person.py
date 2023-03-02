from person import Person


class ResponsiblePerson:
    def __init__(self, person: Person):
        self.person = person

    def drink(self)-> str:
        return self.person.drink() if self.person.age >= 18 else "Muito jovem"
    
    def drive(self) -> str:
        return self.person.drive() if self.person.age >= 16 else "Muito jovem"

    def drink_and_drive(self)-> str:
        if self.drink() == "drinking":
            return self.person.drink_and_drive() + ", Morto"
        else:
            return "Se beber não dirija"

