M_IN_KM = 1000

class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(
        self,
        training_type: str,
        duration: float,
        distance: float,
        speed: float,
        calories: float
        ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        return (f'{self.training_type}; '
                f'Длительность: {self.duration:.3f} ч.; '
                f'Дистанция: {self.distance:.3f} км; '
                f'Ср. скорость: {self.speed:.3f} км/ч; '
                f'Потрачено ккал: {self.calories:.3f}.')


class Training:
    """Базовый класс тренировки."""
    LEN_STEP = 0.65

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        pass

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = action * LEN_STEP / M_IN_KM 
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed: float = self.distance / self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        # возвращает объект класса сообщения.
    

class Running(Training):
    """Тренировка: бег."""
    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79

    def __init__(self, action: int,  duration: float, weight: float):
        super().__init__(action, duration, weight)

    def get_spent_calories(self) -> float:
        spent_calories = (
            (CALORIES_MEAN_SPEED_MULTIPLIER * training.get_mean_speed() 
            + CALORIES_MEAN_SPEED_SHIFT) * self.weight 
            / M_IN_KM * self.duration
            )

class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    CALORIES_COEFFICIENT_1 = 0.035
    CALORIES_COEFFICIENT_2 = 0.029

    def __init__(
        self, action: int,
        duration: float,
        weight: float,
        hight: float
        ):
        super().__init__(action, duration, weight)
        self.hight = hight
    def get_spent_calories(self) -> float:
        spent_calories = (
            (COEFFICIENT_1 * self.weight + (training.get_mean_speed ** 2
            / self.hight) * COEFFICIENT_2 * self.weight) * self.duration
            )

class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP = 1.38
    SWM_CALORIES_COEFFICIENT_1 = 1.1
    SWM_CALORIES_COEFFICIENT_2 = 2
    def __init__(
        self,
        action: int,
        duration: float,
        weight: float,
        length_pool: float,
        count_pool: int
        ):
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        mean_speed = (
            self.length_pool * self.count_pool / M_IN_KM / seelf.duration
            )
        return mean_speed

    def get_spent_calories(self) -> float:
        spent_calories = (
            (swimming.get_mean_speed() * SWM_CALORIES_COEFFICIENT_1)
            * SWM_CALORIES_COEFFICIENT_2 * self.weight * self.duration
            )


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    workout_types = {'SWM' : Swimming,
                     'RUN' : Running,
                     'WLK' : SportsWalking}
    return workout_types[]

def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

