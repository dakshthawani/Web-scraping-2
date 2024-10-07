import time

import requests
import selectorlib
# import sqlite3
import mysql.connector
URL = "https://dakshthawani.github.io/pythonURL/"

# cursor = connection.cursor()
# cursor.execute("select * from events")
# rows = cursor.fetchall()
# print(type(rows))


class Event:
    def scrape(self, url):
        response = requests.get(url)
        source = response.text
        return source

    def extract(self, source):
        extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
        # yaml = yet another markup language
        value = extractor.extract(source)['tours']
        return value

class Email():
    def send(self):
        print("Email sent")


class DatabaseConnection:
    def __init__(self, host="localhost", user="root", password="", database="cityEvents"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
    def connect(self):
        connection = mysql.connector.connect(host=self.host, user=self.user, password = self.password, database =self.database)
        return connection

class Database:

    connection = DatabaseConnection().connect()
    # row = []
    def store(self, extracted):
        for i in extracted:
            row = i.split(",")
            row = [item.strip() for item in row]
            print(row)
            cursor = self.connection.cursor()
            cursor.execute("insert into events values(%s,%s,%s)",row)
            self.connection.commit()
            # with open("data.txt", "w") as file:
        #     file.write(extracted)

    def read(self, extracted):
        for i in extracted:
            row = i.split(",")
            row = [item.strip() for item in row]
            location, city, date = row
            cursor = self.connection.cursor()
            cursor.execute("select * from events where location = ? and city = ? and date = ?", (location, city, date))
            rows = cursor.fetchall()
            return rows


if __name__ == "__main__":
    event = Event()
    scraped = event.scrape(URL)
    extracted = event.extract(scraped)
    print(extracted)
    if extracted != "No upcoming event":
        db = Database()
        rows = db.read(extracted)
        print(rows)
        if not rows:
            db.store(extracted)
            email = Email()
            email.send()
            # time.sleep(300)