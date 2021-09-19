## Fase 2

"""
Descrivi nel linguaggio di programmazione che preferisci un oggetto:

Student con le seguenti proprietà: `firstname` : string, `lastname` : string, `birthdate` : string, `grades` : string

Crea dei metodi d'appoggio sul modello `Student` per calcolare `age` e `avg_grade`
"""

import datetime as dt


class Student:
    def __init__(self, firstname, lastname, birthdate, grades):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.grades = grades

    def age(self):
        today = dt.date.today()
        birthday = dt.datetime.strptime(self.birthdate, '%d-%m-%Y')
        age = today.year - birthday.year
        if today.month - birthday.month > 0:
            return age
        else:
            return age - 1

    def avg_grades(self):
        return sum(int(el) for el in self.grades.split('-')) / len(self.grades)


def main():
    damiano = Student('Damiano', 'Mancini', '14-11-1994', '6-6-7-8-4')
    print(f'Student object as python dictionary {damiano.__dict__}')
    print(f'age: {damiano.age()}')
    print(f'average grades: {damiano.avg_grades()}')


if __name__ == '__main__':
    main()
