class Race:
    def __init__(self, brand, speed, position):
        self.brand = brand
        self.speed = speed
        self.position = position

    def get_position(self):
        return f"{self.brand} is at position {self.position}."
    
    def switch_position(self, new_position):
        self.position = new_position 
        return f"{self.brand} is now at position {self.position}."
    

    def initial_speed(self):
        return f"{self.brand} is at {self.speed}kph."
    
    def speed_up(self, new_speed):
        self.speed = new_speed
        return f" {self.brand} has sped up to {self.speed}kph." 
    
    def slow_down(self, new_speed):
        self.speed = new_speed
        return f"{self.brand} has slown down to {self.speed}kph."
    
cars = [
    Race('Mazda', 90, 2),
    Race('Toyota', 100, 1),
    Race('Honda', 80, 3),
    Race('Ford', 70, 4)
]
cars.sort(key=lambda x: x.speed)
for racers in cars:
    print(racers.get_position())

 


