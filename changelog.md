# Changelog

## [v1.0.0] - 2025-05-05

### Added
- Класс `Light` с поддержкой:
  - Включения и выключения света.
  - Переключения состояния (`toggle()`).
  - Планировщика времени включения/выключения (`set_schedule()` и `check_schedule()`).
  - Поддержки датчика движения (вкл/выкл и реакция на движение).
  - Указания локации (например, `"Кухня"`, `"Спальня"` и т.п.).

- Вложенный класс `ClimateControl`:
  - Управление температурой и влажностью в помещении.
  - Автоматическое включение/выключение обогревателя и увлажнителя.
  - Возможность установки целевых значений температуры и влажности.
  - Возможность включения и отключения авто-режима.
  - Метод `status()` для получения текущего состояния климата в комнате.

### Changed
- Структурировано с соблюдением принципов чистого кода:
  - Явные названия методов и параметров.
  - Добавлена документация к каждой функции.

### Notes
- Это первая стабильная версия базовой системы управления освещением и климатом для умного дома.
- Код пригоден для расширения — возможна интеграция с реальными IoT-устройствами или UI.

