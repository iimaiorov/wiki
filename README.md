# Проект по автоматизации тестирования для мобильного приложения "Wikipedia"

<p align="center">
  <img src="readme/main_page.png" alt="Тестируемая страница" width="400"/>
</p>

## :pencil: Содержание:

- [Используемый стэк](#hammer_and_wrench-используемый-стэк)
- [Реализованные Mobile проверки](#white_check_mark-реализованные-mobile-проверки)
- [Запуск тестов](#arrow_forward-запуск-тестов)
    - [Локально](#локально)
- [Отчеты о прохождении тестов](#bar_chart-отчеты-о-прохождении-тестов)
    - [Allure](#allure)

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

- [x] Отображение результатов поиска
- [x] Открытие страницы из результатов поиска
- [x] Проверка первых четырех экранов Getting Started

## :arrow_forward: Запуск тестов

### Локально
> [!NOTE]
> Ключ `--context` не обязателен, по умолчанию тесты будут запущены на BrowserStack
* Для запуска на реальном устройстве указать ключ `--context=local_real_device`
* Для запуска на виртуальном устройстве указать ключ `--context=local_real_device`
* Для запуска на BrowserStack указать ключ `--context=bstack`

```bash
poetry install
pytest --context=bstack
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

