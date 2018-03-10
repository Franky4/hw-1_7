

class animals:
    paws = None

    def speaks(self):
        sound = None

 class birds(animals):
     wings = 2


class cow(animals):
    paws = 4

    def speaks(self):
        print('Мууууу')

class goat(animals):
    paws = 4

    def speaks(self):
        print('Меееее')

class sheep(animals):
    paws = 4

    def speaks(self):
        print('Беееее')

class pig(animals):
    paws = 4

    def speaks(self):
        print('Хрю-Хрю')

class duck(animals):
    paws = 2

    def speaks(self):
        print('Кря-Кря')

class chicken(animals):
    paws = 2

    def speaks(self):
        print('Ко-ко-ко')

class gees(birds):
    paws = 2
    
    def speaks(self):
        print('Га-га-га')



