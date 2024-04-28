from utils.dal import *
from models.user_model import *

class UserLogic:

    def __init__(self):
        self.dal = DAL()
    
    #functions demanded for facade by project instructions  
    #--------------------------------------------------------------------------------------------  
    def search_user_by_email_password(self,Email,Password):
        sql = f"select * from users where Email ='{Email}' and Password = '{Password}'"
        result = self.dal.get_one_row(sql)
        row = UserModel.dictionary_to_user(result)
        return row

    def insert_user(self,fname , lname , Email, Password):
        roleId = '2'
        sql = "INSERT INTO users(fname,lname,email,password,roleId) values (%s,%s,%s,%s,%s)"
        params =(f'{fname}'.capitalize(),f'{lname}'.capitalize(),Email,Password,roleId)
        new_user= self.dal.insert(sql,params)
        return f'Successfully registered. userId is {new_user}'
 #--------------------------------------------------------------------------------------------  


    # necessary boolean functions for raising exceptions in the facade
    #----------------------------------------------------
    def email_in_system(self, Email):
        sql = "select Email from retreat.users where Email = %s"
        params = (Email,)
        email = self.dal.get_one_row(sql, params)
        return email is not None

        
    def Password_not_in_system(self, password):
        sql = "SELECT Password FROM retreat.users WHERE Password = %s"
        params = (password,)
        result = self.dal.get_table(sql, params)
        return len(result) == 0   

    def close(self):
        self.dal.close()
    
    
  

 
   # def get_all_users(self,):
    #     sql = f'select * from retreat.users '
    #     result = self.dal.get_table(sql)
    #     results = UserModel.dictionaries_to_users(result)
    #     return results

    # def search_user(self,userId = None,fname = None,lname = None,Email = None,Password = None,roleId = None):
    #     sql = f"select * from users where user = {UserModel(userId ,f'{fname}'.upper(),f'{lname}'.upper(),Email ,Password,roleId)}"
    #     result = self.dal.get_one_row(sql)
    #     result = UserModel.dictionary_to_user(result)
    #     return result
    
     # def delete_user(self,userId = None):
    #     sql = f'DELETE FROM users WHERE userId ="{userId}" ;'
    #     result = self.dal.delete(sql)
    #     return result  
    

      
