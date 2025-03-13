from race import Race

def create_cars():
    return [
        Race('Mazda', 90, 2),
        Race('Toyota', 100, 1),
        Race('Honda', 80, 3),
        Race('Ford', 70, 4)
    ]

def sort_cars_by_speed(cars):
    return sorted(cars, key=lambda x: x.speed)

def display_cars(cars):
    for racer in cars:
        print(racer.get_position())
        print("====================================")
        print(racer.initial_speed())
        print("====================================")
        print(racer.speed_up(100))
        print("====================================")

if __name__ == "__main__":
    cars = create_cars()
    sorted_cars = sort_cars_by_speed(cars)
    display_cars(sorted_cars)
