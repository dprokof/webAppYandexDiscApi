# Документация к веб-приложению на Flask для работы с API Яндекс Диска

## Описание

Это веб-приложение на Flask позволяет пользователям просматривать файлы на Яндекс Диске по введенной публичной ссылке (public key) и загружать выбранные файлы на свой компьютер.

## Установка

### Требования

- Python 3.6 или выше
- Flask
- Requests

### Установка зависимостей

Для установки необходимых библиотек установите зависимости из requirements.txt

```bash
pip install -r requirements.txt
```

## Настройка

### Получение OAuth токена

Для работы с API Яндекс Диска необходимо получить OAuth токен. Чтобы получить токен, нужно зарегистрировать
приложение на [Яндекс.OAuth](https://oauth.yandex.ru/)

#### ОЧЕНЬ ВАЖНО!

Для работы с REST API Yandex Cloud нужно предоставить доступ к папке приложения

По умолчанию в окошке "Доступ к данным" такой пункт не высвечивается, нужно обратиться к данным следующим образом:
```commandline
cloud_api:disk.app_folder
```

## Использование

Для запуска используйте 

```commandline
python app.py
```

Приложение будет доступно по адресу 
http://127.0.0.1:5000/

### Интерфейс 

Интерфейс прост, несёт исключительно сопроводительную функцию 

1. Ввод публичной ссылки 
    - На главной странице введите ссылку на Яндекс Диск
2. Просмотр файлов
    - После ввода ссылки приложение отобразит все файлы, доступные по этой ссылке
3. Загрузка файла
    - Нажмите на имя файла для его загрузки на ваш компьютер


### Структура проекта

````
/your_project_directory
│
├── app.py             # Основной файл приложения
└── templates
    ├── index.html     # Шаблон главной страницы
    └── files.html     # Шаблон страницы со списком файлов
````

## Код приложения

get_file_list(public_key): Получает список файлов и папок из API Яндекс Диска по заданной публичной ссылке.

download_file(public_key, file_path): Загружает файл по его пути, используя публичную ссылку.

### Endpoints
````
- /: Главная страница, где пользователь вводит публичную ссылку.
- /files: Обрабатывает POST-запрос с публичной ссылкой и отображает список файлов.
- /download/<path:file_name>: Обрабатывает запрос на скачивание файла.
````

