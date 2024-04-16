class car():
    def __init__(self, marka, model, release):
        self.marka = marka
        self.model = model
        self.release = release
    def present_the_car(self):
      print("Марка авто -", self.marka, "Модель -", self.model, "год выпуска -", self.release)
present_the_car = car("BMV;", "M5;", 2015)
present_the_car.present_the_car()