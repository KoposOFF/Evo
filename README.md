# Парсер через Selenium

## Описание
Краткое описание проекта:
проект позволяет быстро собрать данные в csv файл для дальнейшей их обработки

## Установка
Чтобы установить проект локально, выполните следующие шаги:
Linux: 
1. Установите пакет python3-venv, если он не установлен:
   ~~~bash
   sudo apt install python3-venv
   git clone https://github.com/KoposOFF/Evo.git
   cd имя_репозитория
   python3 -m venv venv
   source venv/bin/activate 
   pip install -r requirements.txt
     запустите код командой:
    python3 main.py

Windows:
1.
  ~~~cmd
    git clone https://github.com/KoposOFF/Evo.git
   cd имя_репозитория
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
запустите код командой:
    python3 main.py
_________________________________________________________________________________________________
В проекте использован прокси сервер, обязательно добавтье файл в корень проекта с именем : ".env"
и укажите в нем:
LOGIN = "Логин"
PASS = "Пароль"
IP = "Ваш ip"
PORT = "Порт"

