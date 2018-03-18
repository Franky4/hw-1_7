import animals

print('Добро пожаловать на ферму!')

duck1 = animals.MyDuck()
duck1.speaks()

for i in range(5):
    duck1.go()

for i in range(5):
    duck1.eat('пшено')

duck1.give()
