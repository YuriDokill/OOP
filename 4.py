class dom():
    def __init__(self, addresses, square, rooms):
        self.addresses = addresses
        self.square = square
        self.rooms = rooms
    def present_the_dom(self):
      print("Адрес -", self.addresses, "Площадь -", self.square, "Количество комнат -", self.rooms)
present_the_dom = dom("Ул.Карла Маркса 107;", '28;', 1)
present_the_dom.present_the_dom()