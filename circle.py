import math


def area(r):
    '''
    Возвращает площадь круга по формуле pi * r**2.

        Параметры:
            r (int | float): радиус круга
        
        Возвращаемое значение:
            (float) : площадь круга

        Пример вызова:
            area(3)  # 28.26
    '''
    if r < 0:
        raise ValueError
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга по формуле 2 * pi * r. 

        Параметры:
            r (int | float): радиус круга
        
        Возвращаемое значение:
            (float) : периметр круга
    
        Пример вызова:
            perimeter(3)  # 18.84
    '''
    if r < 0:
        raise ValueError
    return 2 * math.pi * r

