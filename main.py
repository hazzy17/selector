import sys
import os
sys.path.append(os.path.dirname(__file__))

from race import Race

cars = [
    Race('Mazda', 90, 2),
    Race('Toyota', 100, 1),
    Race('Honda', 80, 3),
    Race('Ford', 70, 4)
]
cars.sort(key=lambda x: x.speed)
for racers in cars:
    print(racers.get_position())
    print("====================================")
    print(racers.initial_speed())
    print("====================================")
    print(racers.speed_up(100))

print("====================================")
print("Cars sorted by speed in ascending order:")
for racers in cars:
    print(racers.get_position())
    print(racers.initial_speed())
    print("====================================")

if __name__ == "__main__":
    pass
# Output:
