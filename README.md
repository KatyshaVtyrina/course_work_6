### 1. Клонирование проекта
1. Зайти в терминал
2. С помощью команды `cd` перейти в директорию, где будет находиться проект
3. Склонировать проект
```bash
git clone https://github.com/KatyshaVtyrina/course_work_6.git
```

### 2. Настройка виртуального окружения

1. Создать виртуальное окружение
```bash
python3 -m venv venv
```
2. Активировать виртуальное окружение
```bash
source venv/bin/activate
```

### 3. Установка зависимостей
1. Перейти в каталог проекта
```bash
cd course_work_6
```
2. Установить зависимости проекта из файла`requirements.txt`
```bash
pip install -r requirements.txt
```

### 4. Установка и настройка Redis
1. Установить
```bash
brew install redis
```
2. Запустить
```bash
redis-server
```

### 5. Установка и настройка PostgreSQL
1. Установить PostreSQL
```bash
brew install postgres
```
2. Подключиться к PostgreSQL от имени пользователя postgres
```bash
psql -U postgres 
```
3. Создать базу данных `mailings`
```bash
CREATE DATABASE mailings;
```
4. Выйти
```bash
\q
```

### 6. Настройка окружения
1. В директории проекте создать файл `.env`

3. Записать в файл следующие настройки
```bash
EMAIL_HOST_USER=адрес электронной почты для аутенфикации на почтовом сервере
EMAIL_HOST_PASSWORD=пароль для аутенфикации на почтовом сервере

DB_USER=имя пользователя (postgres)
DB_NAME=название базы данных (mailings)
SECRET_KEY=секретный ключ 
```
*В проекте есть шаблон файла .env - `.env_exaple`

### 7. Применение миграций
1. Выполнить команду
```bash
python manage.py migrate
```

### 8. Заполнение базы данных
1. Добавить посты
```bash
python manage.py add_posts
```
2. Создать суперпользователя
```bash
python manage.py csu
```

### 9. Запуск celery
1. Открыть новое окно терминала

2. Из каталога проекта запустить celery командой
```bash
celery -A config.celery worker --loglevel=info --pool=solo
```

### 10. Запуск сервера Django
1. Открыть новое окно терминала

2. Запустить сервер
```bash
python manage.py runserver
```

### 11. Работа с приложением
1. Зарегистрироваться
2. Перейти по ссылке, отправленной на электронную почту
3. Создать клиентов
4. Создать сообщение
5. Создать расслыку
