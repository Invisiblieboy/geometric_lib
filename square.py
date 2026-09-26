
def area(a):
    '''
    Возвращает площадь квадрата по формуле a * a. 

        Параметры:
            a (int | float): сторона квадрата
        
        Возвращаемое значение:
            (int | float) : площадь квадрата

        Пример вызова:
            area(3)  # 9
    '''
    if a < 0:
        raise ValueError
    return a * a


def perimeter(a):
    '''
    Возвращает периметр квадрата по формуле 4 * a. 

        Параметры:
            a (int | float): сторона квадрата
        
        Возвращаемое значение:
            (int | float) : периметр квадрата

        Пример вызова:
            perimeter(3)  # 12
    '''
    if a < 0:
        raise ValueError
    return 4 * a
