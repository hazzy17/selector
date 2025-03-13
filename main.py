import game

if __name__ == "__main__":
    print("====================================")
    print("Cars sorted by speed in ascending order:")
    
    # Create, sort, and display the cars
    cars = game.create_cars()
    sorted_cars = game.sort_cars_by_speed(cars)
    game.display_cars(sorted_cars)
