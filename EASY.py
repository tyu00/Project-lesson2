class Car:
    def __init__(self, speed, color, name, is_police):
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


town_car.go()
town_car.turn('налево')
town_car.stop()

sport_car.go()
sport_car.turn('направо')
sport_car.stop()

work_car.go()
work_car.turn('налево')
work_car.stop()

police_car.go()
police_car.turn('направо')
police_car.stop()
