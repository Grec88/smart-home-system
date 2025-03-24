class Light:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            return "Light turned on"
        return "Light is already on"

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            return "Light turned off"
        return "Light is already off"