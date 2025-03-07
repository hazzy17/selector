class Race:
    def __init__(self, brand, speed, position):
        self.brand = brand
        self.speed = speed
        self.position = position

    def get_position(self):
        return f"{self.brand} is at position {self.position} with speed {self.speed}kph."
    
    def switch_position(self, new_position):
        self.position = new_position 
        return f"{self.brand} is now at position {self.position} with speed {self.speed}kph."
    
    def speed_up(self, new_speed):
        self.speed = new_speed
        return f"{self.brand} is now at position {self.position} with speed {self.speed}kph."
    
    def slow_down(self, new_speed):
        self.speed = new_speed
        return f"{self.brand} is now at position {self.position} with speed {self.speed}kph."
    

toyota = Race("Toyota", 100, 1)
print(toyota.get_position())


