import mysql.connector
class Insert():
    def __init__(self) -> None:
        pass
    def insert_data(ocassion, guest, time):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="chatbotdb",
            port="3306"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO event_details (occasion, num_of_guests, time) VALUES (%s, %s, %s)"
        val = (ocassion, guest, time)
        mycursor.execute(sql, val)
        mydb.commit()

if __name__ == "__main__":
    Insert.insert_data("Birthday", "23", "12")

