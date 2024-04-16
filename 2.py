class computer_game():
    def __init__(self, name, developer, release):
        self.name = name
        self.developer = developer
        self.release = release
    def description(self):
      print("Игра -", self.name, "Разработчик -", self.developer, "Год выпуска -", self.release)
description = computer_game("God of War 3;", "idk... ;", 2010)
description.description()