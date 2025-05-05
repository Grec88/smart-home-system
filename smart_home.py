import datetime

class Light:
    def __init__(self, location="Unknown"):
        self.is_on = False
        self.location = location
        self.schedule = []  
        self.motion_sensor_enabled = False

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            return f"{self.location} light turned on"
        return f"{self.location} light is already on"

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            return f"{self.location} light turned off"
        return f"{self.location} light is already off"

    def toggle(self):
        self.is_on = not self.is_on
        return f"{self.location} light toggled to {'on' if self.is_on else 'off'}"

    def set_schedule(self, on_time: str, off_time: str):
        self.schedule = [on_time, off_time]
        return f"Schedule set for {self.location} light: ON at {on_time}, OFF at {off_time}"

    def check_schedule(self):
        now = datetime.datetime.now().strftime("%H:%M")
        if self.schedule:
            on_time, off_time = self.schedule
            if now == on_time:
                return self.turn_on()
            elif now == off_time:
                return self.turn_off()
        return f"No action needed for {self.location} light at {now}"

    def enable_motion_sensor(self):
        self.motion_sensor_enabled = True
        return f"Motion sensor enabled for {self.location} light"

    def detect_motion(self):
        if self.motion_sensor_enabled:
            return self.turn_on()
        return f"Motion detected but sensor is disabled for {self.location} light"
    
    class ClimateControl:
        def __init__(self, location="Unknown", target_temp=22, target_humidity=50):
            self.location = location
            self.current_temp = 22
            self.current_humidity = 50
            self.target_temp = target_temp
            self.target_humidity = target_humidity
            self.heater_on = False
            self.humidifier_on = False
            self.auto_mode = True

    def update_conditions(self, temperature, humidity):
        self.current_temp = temperature
        self.current_humidity = humidity
        return self._auto_adjust()

    def _auto_adjust(self):
        log = []
        if self.auto_mode:
            if self.current_temp < self.target_temp:
                self.heater_on = True
                log.append("Heater turned ON")
            else:
                self.heater_on = False
                log.append("Heater turned OFF")

            if self.current_humidity < self.target_humidity:
                self.humidifier_on = True
                log.append("Humidifier turned ON")
            else:
                self.humidifier_on = False
                log.append("Humidifier turned OFF")
        else:
            log.append("Auto mode is disabled")
        return f"{self.location} climate adjustment: " + "; ".join(log)

    def set_targets(self, temperature, humidity):
        self.target_temp = temperature
        self.target_humidity = humidity
        return f"Target conditions set for {self.location}: Temp {temperature}°C, Humidity {humidity}%"

    def toggle_auto_mode(self):
        self.auto_mode = not self.auto_mode
        return f"Auto mode for {self.location} is now {'enabled' if self.auto_mode else 'disabled'}"

    def status(self):
        return (
            f"Location: {self.location}\n"
            f"Current Temp: {self.current_temp}°C, Target: {self.target_temp}°C\n"
            f"Current Humidity: {self.current_humidity}%, Target: {self.target_humidity}%\n"
            f"Heater: {'ON' if self.heater_on else 'OFF'}\n"
            f"Humidifier: {'ON' if self.humidifier_on else 'OFF'}\n"
            f"Auto Mode: {'ON' if self.auto_mode else 'OFF'}"
        )