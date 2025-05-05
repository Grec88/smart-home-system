class ClimateControl:
    def __init__(self, location="Unknown", target_temp=22, target_humidity=50):
        """
        Инициализация климат-системы.

        :param location: Местоположение устройства.
        :param target_temp: Целевая температура.
        :param target_humidity: Целевая влажность.
        """
        self.location = location
        self.current_temp = 22
        self.current_humidity = 50
        self.target_temp = target_temp
        self.target_humidity = target_humidity
        self.heater_on = False
        self.humidifier_on = False
        self.auto_mode = True

    def update_conditions(self, temperature, humidity):
        """
        Обновить текущие параметры и выполнить автонастройку.

        :param temperature: Текущая температура.
        :param humidity: Текущая влажность.
        :return: Статус изменений.
        """
        self.current_temp = temperature
        self.current_humidity = humidity
        return self._auto_adjust()

    def _auto_adjust(self):
        """
        Автоматически включить или выключить нагреватель и увлажнитель
        на основе текущих и целевых параметров.

        :return: Лог выполненных действий.
        """
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
        """
        Установить целевые параметры климата.

        :param temperature: Новая целевая температура.
        :param humidity: Новая целевая влажность.
        """
        self.target_temp = temperature
        self.target_humidity = humidity
        return f"Target conditions set for {self.location}: Temp {temperature}°C, Humidity {humidity}%"

    def toggle_auto_mode(self):
        """
        Включить или выключить автоматический режим.
        """
        self.auto_mode = not self.auto_mode
        return f"Auto mode for {self.location} is now {'enabled' if self.auto_mode else 'disabled'}"

    def status(self):
        """
        Получить текущий статус климат-контроля.
        """
        return (
            f"Location: {self.location}\n"
            f"Current Temp: {self.current_temp}°C, Target: {self.target_temp}°C\n"
            f"Current Humidity: {self.current_humidity}%, Target: {self.target_humidity}%\n"
            f"Heater: {'ON' if self.heater_on else 'OFF'}\n"
            f"Humidifier: {'ON' if self.humidifier_on else 'OFF'}\n"
            f"Auto Mode: {'ON' if self.auto_mode else 'OFF'}"
        )
