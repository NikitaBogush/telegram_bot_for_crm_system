# Создать образ на основе базового слоя python (там будет ОС и интерпретатор Python).
FROM python:3.10-slim

# Запустить команду создания директории внутри контейнера
RUN mkdir /app

# Скопировать с локального компьютера файл зависимостей
# в директорию /app.
COPY requirements.txt /app

# Выполнить установку зависимостей внутри контейнера.
RUN pip3 install -r /app/requirements.txt --no-cache-dir

# Скопировать содержимое текущей директории 
# c локального компьютера в директорию /app.
COPY . /app

# Сделать директорию /app рабочей директорией. 
WORKDIR /app

# Выполнить запуск бота.
CMD ["python", "telegram_bot.py"]