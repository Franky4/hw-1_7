
class MyAnimals:   # общий класс животные
    paws = None  # лапы
    eyes = 2     # глазка
    life = None  # уровень здоровья
    says = ''   # какой звук издает

    def speaks(self):   # издает звуки
        print(self.says)

    def eat(self):      # кушает
        raise NotImplementedError

    def go(self):  # ходит
        raise NotImplementedError

    def give(self):  # сколько продукции дает животное (молоко, яйца)
        raise NotImplementedError


class MyBirds(MyAnimals):  # Класс птицы
    wings = 2
    paws = 2
    life = 100  # level life

    def eat(self, food):
        if food == 'пшено' or food == 'вода' and self.life < 100:
            self.life += 1
            print('Кушаем. Уровень здоровья - {}'.format(self.life))

    def go(self):
        self.life -= 1
        print('Гуляем. Уровень здоровья - {}'.format(self.life))

    def give(self):
        print('еще одно новое яйцо')


class MyMammal(MyAnimals):  # Класс млекопитающие
    paws = 4
    life = 100

    def eat(self, food):
        if food == 'травка' or food == 'вода':
            if self.life < 100:
                self.life += 1
                print('Уровень здоровья - {}'.format(self.life))

    def go(self):
        self.life -= 2
        print('Уровень здоровья - {}'.format(self.life))

    def give(self):
        print('свежее молоко')


class MyCow(MyMammal):
    says = 'Муууу'


class MyGoat(MyMammal):
    says = 'Мееее'


class MySheep(MyMammal):
    says = 'Беееее'


class MyPig(MyMammal):
    says = 'Хрю-Хрю'

    def eat(self, food):
        if food == 'комбикорм' or food == 'вода':
            if self.life < 100:
                self.life += 1
                print('Уровень здоровья - {}'.format(self.life))
        else:
            self.life -= 1
            print('Уровень здоровья - {}'.format(self.life))

    def go(self):
        self.life -= 3
        print('Уровень здоровья - {}'.format(self.life))

    def give(self):
        self.life = 0
        print('Свежее мясо')


class MyDuck(MyBirds):
    says = 'Кря-Кря'


class MyChicken(MyBirds):
    says = 'Ко-ко-ко'


class MyGees(MyBirds):
    says = 'Га-га-га'
