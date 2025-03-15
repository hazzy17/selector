
print('''
      cars selection
    ====================
        mazda = 0
        toyota = 1
        honda = 2
        ford = 3
    --------------------
''')

def create_cars():
    return [
        {'make': 'Mazda', 'speed': 90, 'position': 2},
        {'make': 'Toyota', 'speed': 100, 'position': 1},
        {'make': 'Honda', 'speed': 80, 'position': 3},
        {'make': 'Ford', 'speed': 70, 'position': 4}
    ]
car = create_cars()
def change_speed():
    for i in range(len(car)):
        print(f"{i}: {car[i]['make']} : {car[i]['speed']}")


speed_changer = int(input("Enter the car: "))
change_speed = car[speed_changer]['speed'] = input("Enter new speed: ")

print(f" {car[speed_changer]['make']} : {car[speed_changer]['speed']}")  # prints the new speed of the car

   






create_cars()
# get_data(pass)

# clean code

def create_cars():
    return [
        {'make': 'Mazda', 'speed': 90, 'position': 2},
        {'make': 'Toyota', 'speed': 100, 'position': 1},
        {'make': 'Honda', 'speed': 80, 'position': 3},
        {'make': 'Ford', 'speed': 70, 'position': 4}
    ]

def display_cars(cars):
    print("\n      Car Selection\n    ====================")
    for index, car in enumerate(cars):
        print(f"    {car['make']} = {index}")
    print("    --------------------\n")

def change_speed(cars):
    display_cars(cars)
    
    while True:
        try:
            car_index = int(input("Enter the car number: "))
            if car_index not in range(len(cars)):
                print("Invalid selection. Try again.")
                continue
            
            new_speed = int(input("Enter new speed: "))  # Ensure it's a number
            cars[car_index]['speed'] = new_speed
            
            print(f"\nUpdated: {cars[car_index]['make']} speed is now {cars[car_index]['speed']} km/h\n")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Main execution
cars = create_cars()
change_speed(cars)
