# Telegram-бот для [CRM-системы](https://github.com/NikitaBogush/crm_system)

![Static Badge](https://img.shields.io/badge/python-3.10-blue?style=for-the-badge) ![Static Badge](https://img.shields.io/badge/python-telegram-bot-21.3-blue?style=for-the-badge) ![Static Badge](https://img.shields.io/badge/aioschedule-0.5.2-blue?style=for-the-badge) 

#### Данный Telegram-бот предназначен для ежедневной отправки сообщения со статистикой за вчерашний день Лидов/Продаж/Суммы сделок. Бот разработан для данной [CRM-системы](https://github.com/NikitaBogush/crm_system). 

#### Развертывание проекта на локальном сервере:
* Для развертывания Бота на вашем локальном сервере должна быть развернута [CRM-система](https://github.com/NikitaBogush/crm_system).
* Клонируем репозиторий
  ```
  git clone https://github.com/NikitaBogush/telegram_bot_for_crm_system
  ```
* Переходим в папку с проектом
  ```
  cd telegram_bot_for_crm_system
  ```  
* Получаем информацию о сети проекта CRM-системы в Docker. 
  ```
  docker network inspect crm_system_default
  ```
* В данной информации находим ключ "Containers", в нем словарь с "Name": "crm_system-nginx-1" и сохраняем значение ключа "IPv4Address".
* В папке с проектом необходимо создать файл .env и указать в нем необходимую информацию
  ```
  Пример заполненного файла:
  AUTHORIZATION_TOKEN = "Bearer YjA0MDRhIiwidXNlcl9pZCI6MX0.cAEm1mtIhj_iTleFPMuQE5R"
  USERNAME = "Admin"
  PASSWORD = "12345"
  TOKEN = "1234556789:UxZL9-Bhk"
  CHAT_ID = "123456789"
  IPV4ADDRESS = "172.19.0.4/16"
  
  AUTHORIZATION_TOKEN - Данный токен можно получить, отправив POST-запрос на эндпоинт "http://127.0.0.1/auth/jwt/create/" и в параметрах запроса указать "username" и "password" суперпользователя CRM-системы. Например {"username": "Admin", "password": "12345"}.
  USERNAME - имя суперпользователя
  PASSWORD - пароль суперпользователя
  TOKEN - токен вашего Telegram-бота
  CHAT_ID - ID пользователя в Telegram, которому отправляются сообщения
  IPV4ADDRESS - значение ключа "IPv4Address", которое было получено ранее
  ```
* Создаем образ Docker
  ```
  docker build -t telegram_bot_image .
  ```
* Запускаем контейнер Docker на основе созданного образа
  ```
  docker run -d --net=crm-system_default --name=telegram_bot telegram_bot_image
  ```