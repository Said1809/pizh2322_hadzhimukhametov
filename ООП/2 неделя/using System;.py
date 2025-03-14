import math

class Автомобиль:
    """
    Базовый класс, представляющий автомобиль.

    Атрибуты:
        x (float): Координата X автомобиля.
        y (float): Координата Y автомобиля.
        angle (float): Угол направления движения в градусах (0 - восток, 90 - север, 180 - запад, 270 - юг).
    """

    def __init__(self, x: float, y: float, angle: float):
        """
        Конструктор класса Автомобиль.

        Args:
            x (float): Начальная координата X.
            y (float): Начальная координата Y.
            angle (float): Начальный угол направления движения.
        """
        self.x = x
        self.y = y
        self.angle = angle

    def move(self, distance: float):
        """
        Перемещает автомобиль на заданное расстояние в текущем направлении.

        Args:
            distance (float): Расстояние для перемещения.
        """
        # Переводим угол из градусов в радианы (необходимо для math.sin и math.cos)
        angle_rad = math.radians(self.angle)

        # Вычисляем изменение координат X и Y на основе угла и расстояния
        dx = distance * math.cos(angle_rad)
        dy = distance * math.sin(angle_rad)

        # Обновляем координаты автомобиля
        self.x += dx
        self.y += dy

    def turn(self, new_angle: float):
        """
        Изменяет угол направления движения автомобиля.

        Args:
            new_angle (float): Новый угол направления в градусах.
        """
        self.angle = new_angle

    def __str__(self):
        """
        Возвращает строковое представление объекта Автомобиль.
        """
        return f"Автомобиль: (X={self.x:.2f}, Y={self.y:.2f}, Угол={self.angle:.2f})"


class Автобус(Автомобиль):
    """
    Дочерний класс, представляющий автобус, унаследованный от класса Автомобиль.

    Атрибуты:
        num_passengers (int): Количество пассажиров в автобусе.
        money_earned (float): Количество денег, заработанных автобусом.

    Дополнительно наследует атрибуты x, y, angle от класса Автомобиль.
    """

    def __init__(self, x: float, y: float, angle: float):
        """
        Конструктор класса Автобус.

        Args:
            x (float): Начальная координата X.
            y (float): Начальная координата Y.
            angle (float): Начальный угол направления движения.
        """
        # Вызываем конструктор базового класса (Автомобиль), чтобы инициализировать x, y и angle
        super().__init__(x, y, angle)  # Важно вызывать super().__init__()

        self.num_passengers = 0  # Изначально в автобусе нет пассажиров
        self.money_earned = 0.0  # Изначально автобус не заработал денег

    def enter(self, num: int):
        """
        Увеличивает количество пассажиров в автобусе.

        Args:
            num (int): Количество пассажиров, вошедших в автобус.
        """
        self.num_passengers += num

    def exit(self, num: int):
        """
        Уменьшает количество пассажиров в автобусе.

        Args:
            num (int): Количество пассажиров, вышедших из автобуса.
        """
        self.num_passengers -= num
        # Проверка, чтобы количество пассажиров не стало отрицательным
        if self.num_passengers < 0:
            self.num_passengers = 0

    def move(self, distance: float):
        """
        Перемещает автобус на заданное расстояние и увеличивает заработок.

        Args:
            distance (float): Расстояние для перемещения.
        """
    
        super().move(distance)

        # Увеличиваем количество денег, заработанных автобусом
        # Например, 0.5 - это плата за проезд за единицу расстояния за одного пассажира
        self.money_earned += self.num_passengers * distance * 0.5

    def __str__(self):
        """
        Возвращает строковое представление объекта Автобус.
        """
        return f"Автобус: (X={self.x:.2f}, Y={self.y:.2f}, Угол={self.angle:.2f}, Пассажиров={self.num_passengers}, Заработано={self.money_earned:.2f})"




#  экземпляр класса Автомобиль
car = Автомобиль(10.0, 20.0, 45.0)
print(car)  

car.move(5.0)
print(car) 

car.turn(90.0)
print(car)  

# экземпляр класса Автобус
bus = Автобус(0.0, 0.0, 0.0)
print(bus)  

bus.enter(10)
print(bus)  

bus.move(10.0)
print(bus)  

bus.exit(5)
print(bus)  

bus.move(5.0)
print(bus)  
