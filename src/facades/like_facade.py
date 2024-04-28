from logic.logic_like import *

class LikeFacade:


    def __init__(self):
            self.logic = LikeLogic()

 # functions demanded by instructions in the project
    #------------------------------------------------------------------------------------
    def add_like (self, userId,vacationId):
        if userId == "" or vacationId == "":
            raise TypeError("All value fields must be filled!")
        elif not str(userId).isnumeric():#if not all characters are digits
            raise ValueError('Value must be integer')
        elif not str(vacationId).isnumeric():#if not all characters are digits
            raise ValueError('Value must be integer')
        elif self.logic.userId_not_in_system(userId):
            raise ValueError("User does not exist in the system")
        elif self.logic.vacationId_not_in_system(vacationId):
            raise ValueError('Vacation is not in system')
        elif self.logic.like_already_exists(userId,vacationId):
            raise ValueError("Like already exists in data base")
        else: 
            addition = self.logic.add_user_like(userId,vacationId) 
            return addition


    def delete_like(self, userId,vacationId): 
        if userId == "" or vacationId == "":
            raise TypeError("All value fields must be filled!")
        elif not f"{userId}".isnumeric():#checks all characters are digits
            raise ValueError('Value must be integer')
        elif not f"{vacationId}".isnumeric():#checks all characters are digits
            raise ValueError('Value must be integer')
        elif self.logic.userId_not_in_system(userId):
            raise ValueError("User does not exist in the system")
        elif self.logic.vacationId_not_in_system(vacationId):
            raise ValueError('Vacation does not exist in the system')
        elif self.logic.vacationId_not_in_likes_table(vacationId):
            raise ValueError('Vacation is not in likes table')
        elif self.logic.userId_not_in_likes_table(userId):
            raise ValueError("User is not in likes table")
        
        else:
             deletion = self.logic.remove_like(userId,vacationId) 
             return deletion
        
#-------------------------------------------------------------------------------------

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.logic.close()
        