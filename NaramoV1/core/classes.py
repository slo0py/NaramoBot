#import pandas as pd
import numpy as np
import math
import mysql.connector
from dotenv import load_dotenv
import os


# technically for efficiency purposes I should make a function to calculate slope and intercept values and then just run another funct to find heat when passing those in so I don't have to constantly recalculate this value every time this is called. 
# However. I am lazy




def calc_heat(excess):
    try:
        excess = math.ceil(excess)
        # Load variables from .env file
        load_dotenv()

        # Connect to MySQL
        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            database=os.getenv('DB_NAME')
        )
        
        cursor = conn.cursor()

        # Fetch Heat and Excess data from training_data
        cursor.execute("SELECT Heat, Excess FROM mytable WHERE Heat IS NOT NULL AND Excess IS NOT NULL")
        data = cursor.fetchall()
        conn.close()

        # Convert to NumPy arrays
        if not data:
            raise ValueError("No data available in the database.")

        heat_vals = np.array([row[0] for row in data])
        excess_vals = np.array([row[1] for row in data])

        # Fit a linear model (Excess = slope * Heat + intercept)
        slope, intercept = np.polyfit(heat_vals, excess_vals, 1)
        estimated_heat = (excess - intercept) / slope
        #delta_excess = 1000 # excess fluctuations

        return (math.ceil(estimated_heat))
    
    except TypeError:
        return ("TypeError")
    
    



def input_values(heat, excess, User_ID):
    load_dotenv()  # Load .env variables

    try:
        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            database=os.getenv('DB_NAME')
        )
        cursor = conn.cursor()

        # Prepare the insert query
        query = """
            INSERT INTO mytable (Heat, Excess, User_ID) 
            VALUES (%s, %s, %s)
        """
        cursor.execute(query, (heat, excess, User_ID))
        conn.commit()

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()



def delete_by_ID(ID_to_delete): # tested - Deletes specific entries
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



def delete_by_User_ID(User_ID):  # UNTESTED - deletes entries based off of user ID
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

        # Delete entries with the specified User_ID
        delete_query = "DELETE FROM mytable WHERE User_ID = %s"
        cursor.execute(delete_query, (User_ID,))
        conn.commit()

        # Reorder IDs to maintain sequential order
        reorder_query = """
            SET @count = 0;
            UPDATE mytable SET ID = (@count := @count + 1) ORDER BY ID;
        """
        for stmt in reorder_query.strip().split(';'):
            if stmt.strip():
                cursor.execute(stmt)
        conn.commit()

    except mysql.connector.Error as err:
        print(f"Error: {err}")  # <-- ADD error handling

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()






    

