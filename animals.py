

class animals:   # общий класс животные
    paws = None  # лапы
    eyes = 2     # глазка
    life = None  # уровень здоровья
    says = ' '   # какой звук издает

    def speaks(self):   # издает звуки
        print(self.says)

    def eat(self):      # кушает
        None

    def go(self):  # ходит
        None

    def give(self): # сколько продукции дает животное (молоко, яйца)
        None


class birds(animals):  # Класс птицы
     wings = 2
     paws = 2
     life = 100  # %

     def eat(self,food):
         if food == 'пшено' or food=='вода':
             if self.life<100:
                 self.life+=1
                 print('Кушаем. Уровень здоровья - {}'.format(self.life))

     def go(self):
         self.life-=1
         print('Гуляем. Уровень здоровья - {}'.format(self.life))

     def give(self):
         print('еще одно новое яйцо')

class mammal(animals):  #  Класс млекопитающие
    paws = 4
    life = 100

    def eat(self,food):
        if food == 'травка' or food=='вода':
            if self.life<100:
                self.life+=1
                print('Уровень здоровья - {}'.format(self.life))
    def go(self):
        self.life-=2
        print('Уровень здоровья - {}'.format(self.life))
    def give(self):
        print('свежее молоко')

class cow(mammal):
    says = 'Муууу'

class goat(mammal):
    says = 'Мееее'

class sheep(mammal):
    says = 'Беееее'

class pig(mammal):
    says = 'Хрю-Хрю'

    def eat(self,food):
        if food == 'комбикорм' or food == 'вода':
            if self.life<100:
                self.life+=1
                print('Уровень здоровья - {}'.format(self.life))
        else:
            self.life-=1
            print('Уровень здоровья - {}'.format(self.life))

    def go(self):
        self.life-=3
        print('Уровень здоровья - {}'.format(self.life))

    def give(self):
        self.life=0
        print('Свежее мясо')


class duck(birds):
    says = 'Кря-Кря'

class chicken(birds):
    says = 'Ко-ко-ко'

class gees(birds):
    says = 'Га-га-га'



