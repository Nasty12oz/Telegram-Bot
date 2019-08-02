from influxdb import InfluxDBClient
import telebot
import time

# bot information
chat_id = 123456789  # your chat id
text = "DB rip. Press F to pay respects"
token = 'bot_token'

# database information
host = 'host'
port = 0000  # your port number
username = 'username'
password = 'password'
database = 'database'


def message():
    lord_kakas = telebot.TeleBot(token=token)
    lord_kakas.send_message(chat_id=chat_id, text=text)


def connection(timeout=1, tries=3):
    client = InfluxDBClient(host=host, port=port, username=username, password=password, database=database)
    for i in range(tries):
        try:
            client.get_list_users()
            print('connection established')
            break
        except Exception:
            time.sleep(timeout)
            if i == tries-1:
                message()
    client.close()


if __name__ == '__main__':
    connection()
