class Toy:
    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type

    def __str__(self):
        return f"Игрушка: {self.name}, Цвет: {self.color}, Тип: {self.toy_type}"


class ToyFactory:
    def create_toy(self, name, color, toy_type):
        print("Закупка сырья...")
        self.purchase_materials()

        print("Пошив игрушки...")
        self.sew_toy()

        print("Окраска игрушки...")
        self.paint_toy()

        return Toy(name, color, toy_type)

    def purchase_materials(self):
        print("Сырьё закуплено.")

    def sew_toy(self):
        print("Игрушка сшита.")

    def paint_toy(self):
        print("Игрушка окрашена.")


if __name__ == "__main__":
    factory = ToyFactory()
    new_toy = factory.create_toy("Медвежонок", "Коричневый", "Животное")
    print(new_toy)
