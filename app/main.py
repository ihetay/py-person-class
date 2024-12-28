class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        if self not in Person.people:
            Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(name=person["name"], age=person["age"]))

    for person in people:
        current_person = Person.people[person["name"]]

        if "wife" in person and person["wife"]:
            wife_instance = Person.people.get(person["wife"])
            if wife_instance:
                current_person.wife = wife_instance

        if "husband" in person and person["husband"]:
            husband_instance = Person.people.get(person["husband"])
            if husband_instance:
                current_person.husband = husband_instance

    return person_list
