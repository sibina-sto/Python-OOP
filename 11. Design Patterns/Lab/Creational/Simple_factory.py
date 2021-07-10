class Car:
    pass


class BMW(Car):
    pass


class Mercedes(Car):
    pass


def simple_car_factory(brand):
    cars = {
        'BMW': BMW,
        'Mercedes': Mercedes,
    }

    return cars[brand]()