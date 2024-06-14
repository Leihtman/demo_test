# demo_ui_pytest_webdriver

<h2> Тестовый проект для тестовых целей. </h2>

<h3> Предварительная настройка окружения включает:  </h3>

1. Установка poetry

```bash
pip3 install poetry
```

2. Установка интерпретатора проекта poetry venv

<h3>Для прогона тестов запустите команду в терминале:</h3>
(рабочая директория при этом должна быть: demo_test)

```bash
pytest --alluredir=allure_results --env_file=.demo.env
```
Посмотреть результаты в allure:
```bash
allure serve allure_results/
```
