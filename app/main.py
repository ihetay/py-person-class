class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    # creating person instances and adding to person_list
    for person in people:
        person_list.append(Person(name=person["name"], age=person["age"]))
    # checking for the presence of the key wife or husband and if found,
    # assign the value wife or husband to the instance
    for person in people:
        current_person = Person.people[person["name"]]

        if wife_name := person.get("wife"):
            current_person.wife = Person.people[wife_name]

        if husband_name := person.get("husband"):
            current_person.husband = Person.people[husband_name]
    # return list
    return person_list
