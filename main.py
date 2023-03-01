from person import Person
from responsible_person import ResponsiblePerson

responsible_person = ResponsiblePerson(Person(10))
print(responsible_person.check_if_drink())
print(responsible_person.check_if_drive())
print(responsible_person.check_if_drink_and_drive())