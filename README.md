# README

test це веб-серсіс для привітань.

## Встановлення
Потрібно встановити requirements.txt та MongoDB для коректної роботи сервісу.

```bash
pip install -r requirements.txt
sudo apt update
sudo apt install -y mongodb
```
Після в терміналі mongo створити таблицю users:
```bash
sudo systemctl start mongodb.service
sudo mongo --shell

> use users
```

## Використання
Щоб запустити сервіс потрібно в терміналі запустити наступну команду:
```bash
uvicorn server.app:app --host 127.0.0.1 --port 8080 --reload
```