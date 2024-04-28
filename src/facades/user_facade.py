from logic.logic_user import *
import re
class UserFacade:


    def __init__(self):
            self.logic = UserLogic()

    # functions demanded by instructions in the project
    #------------------------------------------------------------------------------------
    
    def register_to_system(self,fname , lname , Email, Password):
        if fname == "" or lname == "" or Email == "" or Password == "":#in case user doesn't give a value to a variable
            raise TypeError('You must fill all field values!')   
        elif len(str(fname)) > 45:#confirming sql restriction on value
            raise OverflowError('"First name" must be under 45 characters')
        elif len(str(lname)) > 45:#confirming sql restriction on value
            raise OverflowError('"Last name" must be under 45 characters')
        elif len(str(Email))  > 45:#confirming sql restriction on value
            raise ValueError('"E-mail" must be under 45 characters')
        elif len(str(Password)) > 45:#confirming sql restriction on value
            raise ValueError('"Password" must be under 45 characters')   
        elif not self.valid_name(fname):#if not all characters are letters
            raise ValueError("Only letters,'-','.',''' and spaces allowed")
        elif not self.valid_name(lname):#if not all characters are letters
            raise ValueError("Only letters,'-','.',''' and spaces allowed")
        elif not self.valid_email(Email):
            raise ValueError("Invalid Email address!!!")
        elif len(str(Password)) < 4:
            raise ValueError('Password must be bigger than 4 notes')
        elif self.logic.email_in_system(Email):
            raise ValueError("Email already exist in the system!")
        else:
            user_added = self.logic.insert_user(fname , lname , Email, Password)
            return user_added

            
    def sign_in_for_registered_users(self,Email,Password):
        if Email == "" or Password == "":#in case user doesn't give a value to a variable
            raise TypeError('You must fill all field values!')
        elif len(str(Email))  > 45:#confirming sql restriction on value
            raise OverflowError('"E-mail" must be under 45 characters')
        elif len(str(Password)) > 45:#confirming sql restriction on value
            raise OverflowError('"Password" must be under 45 characters') 
        elif not self.valid_email(Email,):#validation according to email convention pattern
            raise ValueError("Invalid Email address!!!")
        elif len(str(Password,)) < 4:
            raise ValueError('Password must be bigger than 4 notes')
        elif not self.logic.email_in_system(Email):
            raise ValueError("This Email is not registered")
        elif self.logic.Password_not_in_system(Password):
            raise ValueError("Password is not in data base")
        else:
            return f'Your user information is:\n {self.logic.search_user_by_email_password(Email,Password)}'
    #-------------------------------------------------------------------------------------------------------------

    #boolean functions for raising exception in the main functions of the facade
    #-----------------------------------------------------------------------------------------
    def valid_email(self,email):#checks if email is valid according to email pattern
            pattern =  "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$)"
            return bool(re.match(pattern, email))
        
    def valid_name(self,name):
        pattern = r"^[A-Za-z\s\-\'\.\u0590-\u05FF]+$"#allows only letters (hebrew too) and "-",".","'" and spaces.
        return bool(re.match(pattern, name))
    
    #----------------------------------------------------------------------

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.logic.close()
        



