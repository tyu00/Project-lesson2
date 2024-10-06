class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} поехал со скоростью {self.speed} км/ч.")

    def stop(self):
        print(f"{self.name} остановился.")

    def turn(self, direction):
        print(f"{self.name} повернул {direction}.")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


town_car = TownCar(speed=60, color='blue', name='Городской автомобиль')
sport_car = SportCar(speed=130, color='red', name='Спортивный автомобиль')
work_car = WorkCar(speed=80, color='yellow', name='Рабочий автомобиль')
police_car = PoliceCar(speed=100, color='black', name='Полицейский автомобиль')


for car in [town_car, sport_car, work_car, police_car]:
    car.go()
    car.turn('налево')
    car.stop()
