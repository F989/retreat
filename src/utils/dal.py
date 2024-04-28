import mysql.connector

class DAL:

    
    def __init__(self):
            try:
                self.connection = mysql.connector.connect(host="localhost", user="root", password="123456", database="retreat") 
            except mysql.connector.Error as e:
                print("MySQL Connector Error:", e)
            

    
    def get_table(self, sql, params=None):
        with  self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            table = cursor.fetchall()
            return table 
    
    def get_one_row(self, sql, params=None):
        with  self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            row = cursor.fetchone()
            return row 
    
    def insert(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit() # Save to database now.
            last_row_id = cursor.lastrowid
            return last_row_id

    def update(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit() # Save to database now.
            row_count = cursor.rowcount
            return row_count

    def delete(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit() # Save to database now.
            row_count = cursor.rowcount
            return row_count
        
    def insert_v2(self, sql, params=None): #created for addition of like in like table to get addition value
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit() # Save to database now.
            last_row_id = cursor.rowcount
            return last_row_id

    def close(self):
        self.connection.close() 

   


   

            



