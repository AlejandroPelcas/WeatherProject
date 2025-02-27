import sqlite3
from datetime import datetime

DATABASE_NAME = "weather_data.db"


def main():
    conn = sqlite3.connect(DATABASE_NAME)
    curr = conn.cursor()
    curr.execute("SELECT * FROM weather")

    # Fetch all results
    temperatures = curr.fetchall()

    # Print the temperatures
    for temp in temperatures:
        print(temp)  # Each row is a tuple, so access the first element

    conn.commit()
    conn.close()




if __name__ == "__main__":
    main()