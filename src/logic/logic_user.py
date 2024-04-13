from utils.dal import *
from models import user_model

class UserLogic:

    def __init__(self):
        self.dal = DAL()
       

       
    def get_all_users(self,):
        sql = f'select *from retreat.users '
        result = self.dal.get_table(sql)#get dicts
        results = user_model.dictionaries_to_users(result)#convert dict to object
        return results
        
    def search_user(self,userId = None,fname = None,lname = None,Email = None,Password = None,roleId = None):
        sql = f"select * from users where user = {user_model(userId ,fname,lname,Email ,Password,roleId)}"
        result = self.dal.get_table(sql)#get dicts
        results = user_model.dictionaries_to_users(result)#convert dict to object
        return results
    
    def search_user_by_email_password(self,Email = None,Password = None):
        sql = f"select * from users where Email ='{Email}' and Password = '{Password}'"
        result = self.dal.get_table(sql)#get dicts
        results = user_model.dictionaries_to_users(result)#convert dict to object
        return results

    def insert_user(self,fname , lname , Email, Password, roleId ):
        sql = f"INSERT INTO users(fname,lname,email,password,roleId) values ('{fname}','{lname}','{Email}','{Password}','{roleId}')"
        result = self.dal.insert(sql)#get dicts
        return result
    
    


    def update_user(self, fname,lname,email,password):
        pass

    def delete_user(self,userId = None):
        sql = f'DELETE FROM users WHERE userId ="{userId}" ;'
        result = self.dal.delete(sql)
        return result
    
    def fetch_one_user(self, fname = None, lname = None, Email = None):
        pass 
    
    def fetch_all_users_order_by(self, fname = None, lname = None, Email = None):
        pass
    def email_in_system(self,Email):
        pass

      
