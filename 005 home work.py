# TODO:Реализовать класс Person, у которого должно быть два публичных поля: age и name.
# Также у него должен быть следующий набор методов: know(person), который позволяет
# добавить другого человека в список знакомых. И метод is_known(person), который возвращает знакомы ли два человека


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.known_pers = []

    def know(self, somebody):
        if somebody in self.known_pers:
            print(f'{self.name} alredy knowns {somebody.name}')
        else:
            self.known_pers.append(somebody)

    def is_know(self, somebody):
        if somebody in self.known_pers:
            print(f'{self.name} knowns {somebody.name}')
        else:
            print(f'{somebody.name} eto che  za huy')

    @staticmethod
    def count():
        return 'some'

def main():
    vasya = Person('Vasya', 35)
    grisha = Person('Grisha', 38)
    petya = Person('Petya', 45)

    print(Person.count())

    vasya.know(grisha)
    vasya.know(petya)
    vasya.know(petya)
    petya.know(vasya)
    petya.is_know(vasya)
    petya.is_know(grisha)

if __name__ == '__main__':
    main()

