from race import Race
from admin import create_cars


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
