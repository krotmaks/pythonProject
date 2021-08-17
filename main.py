class Person:
    name = "name"
    age = 0
    def add(self, name, age):
        self.name = name
        self.age = age
maks = Person()
ilya = Person()
ilya.add("Ilya", 22)
maks.add("Maks", 31)
print(ilya.name + " " + str(ilya.age))
print(maks.name + " " + str(maks.age))



