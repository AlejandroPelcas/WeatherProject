import sqlite3

DATABASE_NAME = "weather_data.db"

def main():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM weather")
    data = cursor.fetchall()
    # Print the temperatures
    for temp in data:
        print(temp)  # Each row is a tuple, so access the first element


    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()