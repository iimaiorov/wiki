# Проект по тестированию приложения "Wikipedia"

<p align="center">
  <img src="readme/main_page.png" alt="Тестируемая страница" width="400"/>
</p>

## :pencil: Содержание:

- [Используемый стэк](#hammer_and_wrench-используемый-стэк)
- [Реализованные Mobile проверки](#white_check_mark-реализованные-mobile-проверки)
- [Запуск тестов](#arrow_forward-запуск-тестов)
    - [Jenkins](#jenkins)
    - [Локально](#локально)
- [Отчеты о прохождении тестов](#bar_chart-отчеты-о-прохождении-тестов)
    - [Allure](#allure)
    - [Telegram](#telegram)

### :hammer_and_wrench: Используемый стэк

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Pytest](https://img.shields.io/badge/Pytest-29B6F6?style=for-the-badge&logo=pytest&logoColor=white)
![Selene](https://img.shields.io/badge/Selene-42b029?style=for-the-badge)
![Jenkins](https://img.shields.io/badge/Jenkins-000?style=for-the-badge&logo=jenkins&logoColor=white)
![PyCharm](https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white)
![Jira](https://img.shields.io/badge/Jira-0052CC?style=for-the-badge&logo=Jira&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Allure](https://img.shields.io/badge/Allure-21c55d?style=for-the-badge)
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)

### :white_check_mark: Реализованные Mobile проверки

[x] Отображение результатов поиска
[x] Открытие страницы из результатов поиска
[x] Проверка первых четырех экранов Getting Started

## :arrow_forward: Запуск тестов

### Локально

1. Склонировать репозиторий
2. Открыть проект и установить интерпретатор
3. Создать файл с переменными окружения `.env.bstack`,  `.env.local_real` или `.env.local_emulator` в зависимости от
   того, какое окружение хотите использовать, по образцу в корне проекта
4. Запустить тесты

Можно запускать тесты на BrowserStack:

```bash
pytest --context=bstack
```

локально через эмулятор:

```bash
pytest --context=local_emulator
```

локально через реальное устройство:

```bash
pytest --context=local_real
```

## :bar_chart: Отчеты о прохождении тестов

### Allure

Для просмотра отчета локально нужно ввести команду:

```bash
allure serve
```

Примеры отображения тестов:

![Отчет в Allure](/readme/allure_1.png)

![Отчет в Allure](/readme/allure_2.png)

