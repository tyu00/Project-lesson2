class Toy:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"Игрушка: {self.name}, Цвет: {self.color}"


class AnimalToy(Toy):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.toy_type = "Животное"

    def __str__(self):
        return f"{super().__str__()}, Тип: {self.toy_type}"


class CharacterToy(Toy):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.toy_type = "Персонаж мультфильма"

    def __str__(self):
        return f"{super().__str__()}, Тип: {self.toy_type}"


class ToyFactory:
    def create_toy(self, name, color, toy_type):
        print("Закупка сырья...")
        self.purchase_materials()

        print("Пошив игрушки...")
        self.sew_toy()

        print("Окраска игрушки...")
        self.paint_toy()

        if toy_type == "Животное":
            return AnimalToy(name, color)
        elif toy_type == "Персонаж мультфильма":
            return CharacterToy(name, color)
        else:
            raise ValueError("Неизвестный тип игрушки.")

    def purchase_materials(self):
        print("Сырьё закуплено.")

    def sew_toy(self):
        print("Игрушка сшита.")

    def paint_toy(self):
        print("Игрушка окрашена.")


if __name__ == "__main__":
    factory = ToyFactory()

    animal_toy = factory.create_toy("Медвежонок", "Коричневый", "Животное")
    print(animal_toy)

    character_toy = factory.create_toy("Супермен", "Красный", "Персонаж мультфильма")
    print(character_toy)
