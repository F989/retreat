from utils.dal import * 
from models.vacation_model import * 
from models.country_vacation_model import *

class VacationLogic :
    def __init__(self):
        self.dal = DAL()
    

    def get_all_vacations(self):
        sql = "select*from retreat.vacations"
        result= self.dal.get_table(sql) # get dicts 
        results = VacationModel.dictionaries_to_vacations(result) # convet dict to object 
        return results 
    

    def create_new_vacation(self, v_description=None, start_date=None, last_day_date=None, price=None, vacation_pic=None, countryId=None):
      sql = "INSERT INTO vacations (v_description, start_date, last_day_date, price, vacation_pic, countryId) VALUES (%s, %s, %s, %s, %s, %s)"
      params = (v_description, start_date, last_day_date, price, vacation_pic, countryId)
      row_count = self.dal.insert(sql, params)
      return row_count   

    '''
    def create_new_vacation(self, country, price, start_date, last_day_date):
       sql = "INSERT INTO vacations (country, price, start_date,last_day_date ) VALUES (%s, %s, %s, %s)"
       params = (country, price, start_date, last_day_date)
       return self.dal.insert(sql, params)
    '''

    def update_vacation(self, vacationId = None,v_description = None, start_date = None, last_day_date = None, price = None,vacation_pic = None,countryId=None ):
        sql = "UPDATE vacations SET v_description= %s, start_date = %s last_day_date= %s  price = %s vacation_pic=%s countryId=None %s WHERE vacationId = %s"
        params = (vacationId,v_description,start_date ,last_day_date,price, vacation_pic,countryId)
        row_count = self.dal.update(sql, params)
        return row_count
    
    
    


    def delete_vacation(self, vacation_id):
        sql = "DELETE FROM vacations WHERE vacationId = %s"
        params = (vacation_id,)
        row_count = self.dal.delete(sql, params)
        return row_count


    def get_vacation_by_country(self, country):
      sql = "SELECT retreat.vacations.vacationId,retreat.vacations.v_description,retreat.vacations.start_date,retreat.vacations.last_day_date,retreat.vacations.price,retreat.vacations.vacation_pic,retreat.vacations.countryId,retreat.countries.country   FROM retreat.vacations left join retreat.countries  on retreat.vacations.countryId=retreat.countries.countryId WHERE country = %s"
      params = (country,)
      result = self.dal.get_table(sql, params)
      if result:
        return CountryModel.dictionaries_to_vacations(result)
      else:
        return None
    '''
    def get_vacation_by_country_v2(self, country):
      sql = "SELECT retreat.vacations.vacationId,retreat.vacations.v_description,retreat.vacations.start_date,retreat.vacations.last_day_date,retreat.vacations.price,retreat.vacations.vacation_pic,retreat.vacations.countryId,retreat.countries.country   FROM retreat.vacations left join retreat.countries  on retreat.vacations.countryId=retreat.countries.countryId WHERE country = %s"
      params = (country,)
      result = self.dal.get_table(sql, params)
      if result:
        return (result)
      else:
        return None
       '''
    def get_vacation_by_price(self, price):
      sql = "SELECT * FROM retreat.vacations WHERE price <= %s"
      params = (price,)
      result = self.dal.get_table(sql, params)
      results = VacationModel.dictionary_to_vacation(result)
      return results
   
   
    def update_vacation_price(self, vacationId = None, price = None ):
        sql = "UPDATE vacations SET price = %s WHERE vacationId = %s"
        params = (vacationId,price)
        row_count = self.dal.update(sql, params)
        return row_count
    
    def get_vacation_by_date(self, start_date, end_date):
       sql = "SELECT * FROM retreat.vacations WHERE date BETWEEN %s AND %s"
       params = (start_date, end_date)
       result = self.dal.get_table(sql, params)
       results = VacationModel.dictionary_to_vacation(result)
       return results
    
    
    def update_vacation_date(self, vacationId = None,start_date = None, last_day_date = None ):
        sql = "UPDATE vacations SET start_date = %s last_day_date= %s WHERE vacationId = %s"
        params = (vacationId,start_date ,last_day_date)
        row_count = self.dal.update(sql, params)
        return row_count 
    





