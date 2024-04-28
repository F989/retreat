from utils.dal import *
from models.like_model import *
from models.user_model import *
from models.vacation_model import *

class LikeLogic:

    def __init__(self):
        self.dal = DAL() 
        
 #functions demanded for facade by project instructions  
    #--------------------------------------------------------------------------------------------
    def add_user_like(self, userId,vacationId):
        sql = "INSERT INTO likes(userId,vacationId) VALUES (%s,%s)"
        params =(userId,vacationId)
        addition = self.dal.insert_v2(sql,params)
        return f'{addition} like has been added in the data base '
    
    def remove_like(self,userId, vacationId):
        sql = 'DELETE FROM likes WHERE userId = %s and vacationId = %s ;'
        params = (userId,vacationId)
        row_count = self.dal.delete(sql, params)
        return f'{row_count} like successfully deleted from data base'
    
     #------------------------------------------------------------------------------------------------

    
    # necessary boolean functions for raising exceptions in the facade
    #-----------------------------------------------------
    
    def vacationId_not_in_system(self,vacationId):
        sql = "select vacationId from retreat.vacations where vacationId = %s"
        params = (vacationId,)
        vacation = self.dal.get_one_row(sql, params)
        return vacation is None

    def userId_not_in_system(self,userId):
        sql = "select userId from retreat.users where userId = %s"
        params = (userId,)
        user = self.dal.get_one_row(sql, params)
        return user is None
 
    def vacationId_not_in_likes_table(self,vacationId):
        sql = 'select * from retreat.likes where vacationId = %s '
        params = (vacationId,)
        like_vacationId = self.dal.get_one_row(sql, params)
        return  like_vacationId is None
    
    def userId_not_in_likes_table(self,userId):
        sql = 'select * from retreat.likes where userId = %s '
        params = (userId,)
        like_userId = self.dal.get_one_row(sql, params)
        return like_userId is None
        
    def like_already_exists(self,userId,vacationId):
        sql = 'select * from retreat.likes where userId = %s and vacationId = %s '
        params = (userId,vacationId)
        like = self.dal.get_one_row(sql, params)
        return bool(like) 
    
#------------------------------------------------------------------------------

    def close(self):
        self.dal.close()