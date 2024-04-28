from logic.logic_vacation import *
from datetime import datetime 
import re

class VacationFacade:
    
    def __init__(self):
        self.logic = VacationLogic()

    

    # functions demanded by instructions in the project
    #------------------------------------------------------------------------------------

    def get_all_vacation_ordered_by_date(self,):
        return self.logic.get_all_vacation_ordered_by_date()

    
    def create_new_vacation(self, v_description, start_date, last_day_date, price,countryId,vacation_pic=None):
        if start_date > last_day_date:
           raise ValueError("Start date must be before last day date")
        elif 0 >= float(price) >= 10000 :
            raise ValueError("Price must be between 0 and 10000")
        elif len(str(v_description)) > 255:
            raise OverflowError("No more then 255 characters are allowed ")
        elif len(str(vacation_pic)) > 255:
            raise OverflowError("No more then 255 characters are allowed ")
        elif v_description=="" or start_date=="" or last_day_date=="" or price == "" or countryId=="":
            raise TypeError("Field value not found.you must fill description start date,departure date,price and countryId ")
        elif self.price_pattern_not_valid(price):
           raise ValueError("Price must consist of only digits and may have a float point")
        elif self.incorrect_date_pattern(start_date) : 
            raise ValueError("Start date incorrect pattern must be YYYY-MM-DD ")
        elif self.incorrect_date_pattern(last_day_date) : 
            raise ValueError("Departure date incorrect pattern must be YYYY-MM-DD ")
        elif not (str(countryId).isnumeric()):
           raise ValueError("Only digits for countryId")
        elif self.logic.countryId_does_not_exist(countryId):
           raise ValueError("CountryId does not exist in data base")
        elif self.start_date_is_history(start_date):
            raise ValueError("Date must be equal or after current date")
        else: 
            return self.logic.create_new_vacation(v_description, start_date, last_day_date, price, vacation_pic, countryId)
        

        
    def update_vacation(self, vacationId=None, v_description=None, start_date=None, last_day_date=None, price=None, vacation_pic=None, countryId=None):
        
        if vacationId == "":#
            raise TypeError("VacationId was not input")#
        elif v_description == '' and start_date == '' and last_day_date == '' and price == '' and vacation_pic == '' and countryId == '':
             raise TypeError("At least one update field has to be input")#
        elif self.price_pattern_not_valid(price):#
           raise ValueError("Price must consist of only digits and may have a float point")
        elif 0 >= float(price) >= 10000 :#
            raise ValueError("Price must be between 0 and 10000")
        elif len(str(v_description)) > 255:#
            raise OverflowError("No more then 255 characters are allowed ")
        elif len(str(vacation_pic)) > 255:#
            raise OverflowError("No more then 255 characters are allowed ")
        elif not (str(vacationId).isnumeric()):#
            raise ValueError("Only digits for vacationId")
        elif self.logic.vacationId_not_in_system(vacationId):#
            raise ValueError('Vacation not in system')
        elif self.incorrect_date_pattern(last_day_date) : #
            raise ValueError("Departure-date incorrect pattern must be YYYY-MM-DD ")
        elif self.incorrect_date_pattern(start_date) : 
            raise ValueError("Start-date incorrect pattern must be YYYY-MM-DD ")
        elif start_date > last_day_date:#
           raise ValueError("Start-date must be before departure date")
        elif not (str(countryId).isnumeric()):#
            raise ValueError("Only digits for countryId")
        elif self.logic.countryId_does_not_exist(countryId):#
            raise ValueError("CountryId does not exist in data base") 
        elif self.start_date_is_history(start_date):#
            raise ValueError("Date must be equal or after current date")
        
        else:
            return self.logic.update_vacation(vacationId, v_description, start_date, last_day_date, price, vacation_pic, countryId)

    def delete_vacation(self, vacationId):
        if vacationId == "":
            raise TypeError("VacationId was not input")#
        elif not (str(vacationId).isnumeric()):#
            raise ValueError("Only digits for vacationId")
        elif self.logic.vacationId_not_in_system(vacationId):
            raise ValueError('Vacation not in system')
        
        return self.logic.delete_vacation(vacationId)
    
    #functions for raising exception in the main functions of the facade
    #-----------------------------------------------------------------------------------------
    def start_date_is_history(self,start_date):#checks if date variable is before current date
        current_date = datetime.now().date()
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()#change pattern to fit datetime library (making sure)
        return current_date < start_date
    
    def vacationId_not_in_system(self,vacationId=None):
       return vacationId is None 
          
    def price_pattern_not_valid(self,price):
        price_pattern = r'^\d+(\.\d{2})?$'
        return not re.match(price_pattern, price)#check if price variable ,matches correct pattern
   

    def incorrect_date_pattern(self,date):
        date_pattern = r'^\d{4}-\d{2}-\d{2}$'  # YYYY-MM-DD format
        return not re.match(date_pattern, date) #check if date variable ,matches correct pattern
    #--------------------------------------------------------------------------------------------------------------

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.logic.close()



        # def get_future_vacations(self, vacationId=None, start_date=None, last_day_date=None):
        # if vacationId is None or start_date is None or last_day_date is None:
        #    raise ValueError("All values must be provided")
        # current_date = datetime.now().date()
        # start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        # last_day_date = datetime.strptime(last_day_date, "%Y-%m-%d").date()
        # if start_date >= current_date:
           
        #     return self.logic.get_future_vacations( start_date, last_day_date,vacationId)
        # else:
        #   return "The start date must be in the future"

 # def update_vacation_date(self, vacationId=None, start_date=None, last_day_date=None):
    #     if self.incorrect_date_pattern(start_date) : 
    #         raise ValueError("start date incorrect pattern must be YYYY-MM-DD ")
    #     elif self.incorrect_date_pattern(last_day_date) : 
    #         raise ValueError("departure date incorrect pattern must be YYYY-MM-DD ")
    #     elif self.logic.vacationId_not_in_system(vacationId):
    #         raise ValueError('Vacation not in system')
    #     else:
    #         return self.logic.update_vacation_date(vacationId, start_date, last_day_date)        