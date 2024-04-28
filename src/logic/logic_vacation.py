from utils.dal import * 
from models.vacation_model import * 
from models.country_vacation_model import *

class VacationLogic :
    def __init__(self):
        self.dal = DAL()

    #functions demanded for facade by project instructions  
    #--------------------------------------------------------------------------------------------
    def get_all_vacation_ordered_by_date(self,):
        sql = "SELECT * FROM vacations ORDER BY start_date, last_day_date ASC"
        table = self.dal.get_table(sql)
        rows = VacationModel.dictionaries_to_vacations(table)
        return rows

    def create_new_vacation(self, v_description, start_date, last_day_date, price, countryId,vacation_pic=None):
      sql = "INSERT INTO vacations (v_description, start_date, last_day_date, price, vacation_pic, countryId) VALUES (%s, %s, %s, %s, %s, %s)"
      params = (v_description, start_date, last_day_date, price, vacation_pic, countryId)
      row_count = self.dal.insert(sql, params)
      return f'{row_count} Vacation successfully created'   

 
    def update_vacation(self, vacationId = None,v_description = None, start_date = None, last_day_date = None, price = None,vacation_pic = None,countryId=None ):
        sql = "UPDATE vacations SET v_description= %s, start_date = %s last_day_date= %s  price = %s vacation_pic=%s countryId=None %s WHERE vacationId = %s"
        params = (vacationId,v_description,start_date ,last_day_date,price, vacation_pic,countryId)
        row_count = self.dal.update(sql, params)
        return f'{row_count} Vacation successfully updated'
    
    
    def delete_vacation(self, vacationId):
        sql = "DELETE FROM vacations WHERE vacationId = %s"
        params = (vacationId,)
        row_count = self.dal.delete(sql, params)
        return f' {row_count} Vacation successfully deleted'
    #------------------------------------------------------------------------------------------------

    
    # necessary boolean functions for raising exceptions in the facade
    #-----------------------------------------------------
    def vacationId_not_in_system(self,vacationId):
        sql = "select vacationId from retreat.vacations where vacationId = %s"
        params = (vacationId,)
        vacationId = self.dal.get_one_row(sql, params)
        return vacationId is None
    
    def countryId_does_not_exist(self,countryId):
        sql="select countryId from retreat.countries where countryId = %s"
        params =(countryId,)
        countryId = self.dal.get_one_row(sql, params)
        return countryId is None
    #------------------------------------------------------------


    def close(self):
            self.dal.close()


# def get_vacation_by_country(self, country):
    #   sql = "SELECT retreat.vacations.vacationId,retreat.vacations.v_description,retreat.vacations.start_date,retreat.vacations.last_day_date,retreat.vacations.price,retreat.vacations.vacation_pic,retreat.vacations.countryId,retreat.countries.country   FROM retreat.vacations left join retreat.countries  on retreat.vacations.countryId=retreat.countries.countryId WHERE country = %s"
    #   params = (country,)
    #   result = self.dal.get_table(sql, params)
    #   if result:
    #     return CountryModel.dictionaries_to_vacations(result)
    #   else:
    #     return None
    
    # def get_vacation_by_price(self, price):
    #   sql = "SELECT * FROM retreat.vacations WHERE price >= %s"
    #   params = (price,)
    #   result = self.dal.get_table(sql, params)
    #   results = VacationModel.dictionaries_to_vacations(result)
    #   return results
   
   
    # def update_vacation_price(self,vacationId = None, price = None ):
    #     sql = "UPDATE vacations SET price = %s WHERE vacationId = %s"
    #     params = (price,vacationId)
    #     row_count = self.dal.update(sql, params)
    #     return row_count

    #  def get_all_vacations(self):
    #     sql = "select*from retreat.vacations ordered by "
    #     result= self.dal.get_table(sql) # get dicts 
    #     results = VacationModel.dictionaries_to_vacations(result) # convert dict to object 
    #     return results 

    # def get_future_vacations(self , vacationId=None,start_date=None, last_day_date=None):
    #    sql = "SELECT * FROM retreat.vacations WHERE start_date = %s AND last_day_date = %s AND vacationId = %s"
    #    params = (vacationId,start_date, last_day_date, )
    #    result = self.dal.get_table(sql, params)
    #    results = VacationModel.dictionaries_to_vacations(result)
    #    return results
    
    # def update_vacation_date(self, vacationId = None,start_date = None, last_day_date = None ):
    #     sql = "UPDATE vacations SET start_date = %s, last_day_date = %s WHERE vacationId = %s"
    #     params = (start_date ,last_day_date,vacationId)
    #     row_count = self.dal.update(sql, params)
    #     return row_count 





