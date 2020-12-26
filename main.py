class Critter(object):
    """Класс для виртуальной зверушки"""
    # иницилизирующвя функция
    def __init__(self, name, hungre = 0, boredom = 0):
        self.name = name
        self.hunger = hungre
        self.boredom = boredom
    # функция имитации времени
    def __pass_time(self):
        self.boredom += 1
        self.hunger += 1

