import datetime

class Light:
    def __init__(self, location="Unknown"):
        """
        Инициализация объекта освещения.

        :param location: Местоположение источника света.
        """
        self.is_on = False
        self.location = location
        self.schedule = []
        self.motion_sensor_enabled = False

    def turn_on(self):
        """
        Включить свет, если он ещё не включён.
        """
        if not self.is_on:
            self.is_on = True
            return f"{self.location} light turned on"
        return f"{self.location} light is already on"

    def turn_off(self):
        """
        Выключить свет, если он включён.
        """
        if self.is_on:
            self.is_on = False
            return f"{self.location} light turned off"
        return f"{self.location} light is already off"

    def toggle(self):
        """
        Переключить состояние света (вкл/выкл).
        """
        self.is_on = not self.is_on
        return f"{self.location} light toggled to {'on' if self.is_on else 'off'}"

    def set_schedule(self, on_time: str, off_time: str):
        """
        Установить расписание включения и выключения.

        :param on_time: Время включения (строка "HH:MM").
        :param off_time: Время выключения (строка "HH:MM").
        """
        self.schedule = [on_time, off_time]
        return f"Schedule set for {self.location} light: ON at {on_time}, OFF at {off_time}"

    def check_schedule(self):
        """
        Проверить текущее время и включить/выключить свет по расписанию.
        """
        now = datetime.datetime.now().strftime("%H:%M")
        if self.schedule:
            on_time, off_time = self.schedule
            if now == on_time:
                return self.turn_on()
            elif now == off_time:
                return self.turn_off()
        return f"No action needed for {self.location} light at {now}"

    def enable_motion_sensor(self):
        """
        Включить реагирование на движение.
        """
        self.motion_sensor_enabled = True
        return f"Motion sensor enabled for {self.location} light"

    def detect_motion(self):
        """
        Обработать событие движения.
        """
        if self.motion_sensor_enabled:
            return self.turn_on()
        return f"Motion detected but sensor is disabled for {self.location} light"
