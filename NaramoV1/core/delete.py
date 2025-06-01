import numpy as np
import math
import mysql.connector
from dotenv import load_dotenv
import os


def delete_and_reorder(id_to_delete):
    load_dotenv()  # Load environment variables

    conn = None
    cursor = None

    try:
        # Connect to the database
        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            database=os.getenv('DB_NAME')
        )
        cursor = conn.cursor()

        # Delete the entry with the specified ID
        delete_query = "DELETE FROM mytable WHERE ID = %s"
        cursor.execute(delete_query, (id_to_delete,))
        conn.commit()
        print(f"Deleted entry with ID {id_to_delete}")

        # Update IDs for rows with higher IDs to fill the gap
        update_query = """
            UPDATE mytable
            SET ID = ID - 1
            WHERE ID > %s
        """
        cursor.execute(update_query, (id_to_delete,))
        conn.commit()
        print(f"Updated IDs of entries with ID > {id_to_delete}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

guh = input("what delete: ")
delete_and_reorder(guh)