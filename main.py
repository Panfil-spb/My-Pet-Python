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


    # функция которая возвращает настроение питомца
    @property
    def mood(self):
        happy = self.hunger + self.boredom
        if happy < 5:
            m = "отлично"
        elif 5 <= happy <= 10:
            m = "неплохо"
        elif 11 <= happy <= 15:
            m = "плохо"
        elif 16 <= happy <= 20
            m = "ужасно"
        return m

    def talk(self):
        print("Привет! Меня зовут " + self.name + ". Сейчас я себя чувствую себя " + self.mood + ".")
        self.__pass_time()

    def feeding(self):
