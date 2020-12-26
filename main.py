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
        elif 16 <= happy <= 20:
            m = "ужасно"
        return m

    def talk(self):
        print("Привет! Меня зовут " + self.name + ". Сейчас я себя чувствую себя " + self.mood + ".")
        self.__pass_time()

    def feeding(self, food = 4):
        print("Мрррр... Спасибо!")
        self.hunger -= food
        self.__pass_time()
        if self.hunger < 0:
            self.hunger = 0

    def play(self, game = 4):
        print("Уиии!")
        self.boredom -= game
        self.__pass_time()
        if(self.boredom < 0):
            self.boredom = 0

def menu():
    print("\tМеню\n"
          "1 - Узнать как дела\n"
          "2 - Поиграть\n"
          "3 - Покормить\n"
          "0 - Выход\n")


def main():
    while 1:
        Name = str(input("Введите имя вашего питомца: "))
        if Name == "":
            print("У вашего питомца должно быть имя!")
        else:
            break
    myPet = Critter(Name)
    myPet.talk()
    while 1:
        menu()
        choise = str(input("Ваш выбор: "))
        if choise == '1':
            myPet.talk()
        elif choise == '2':
            myPet.play()
        elif choise == '3':
            myPet.feeding()
        elif choise == '0':
            print("\nДосвидания!")
            break
        else:
            print("\nВведите номер из списка!\n")


main()
