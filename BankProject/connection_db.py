import mysql.connector

def connect_to_db():
   return mysql.connector.connect(
       host="localhost",
       user="root",
       password="admin",
       database="MagadhaBank"
   )

################################################
con = connect_to_db()  # Call the function to establish the connection

if con.is_connected():
    print("Successfully connected to the database!")
    con.close()  # Close the connection after checking
else:
    print("Failed to connect!")


