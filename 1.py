class subject():
    def __init__(self, subjectName, name, hours):
        self.subjectName = subjectName
        self.name = name
        self.hours = hours
    def subject_descriptions(self):
      print("Название предмета -", self.subjectName, "Имя преподавателя -", self.name, "Количество часов -", self.hours)
subject_descriptions = subject("Алгоритмизация,", "Пухов,", 69)
subject_descriptions.subject_descriptions()