class CountryModel:
     


    def __init__(self,vacationId,country,v_description,start_date,last_day_date,price,vacation_pic):
     
            self.vacationId = vacationId
            self.country = country
            self.v_description = v_description
            self.start_date = start_date
            self.last_day_date = last_day_date
            self.price = price
            self.vacation_pic = vacation_pic

    def __str__(self):
         return  (f"vacationId: {self.vacationId} country:{self.country} v_description:{self.v_description} self.start_date:{self.start_date} "
                f"last_day_date: {self.last_day_date} price:{self.price} vacation_pic:{ self.vacation_pic} " )

    
    @staticmethod
    def dictionary_to_vacation(dictionary):
        if dictionary is None:#to prevent system crash when sql has no result
            return None
        vacationId = dictionary.get("vacationId")
        country =  dictionary.get("country")
        v_description =  dictionary.get("v_description")
        start_date =  dictionary.get("start_date")
        last_day_date =  dictionary.get("last_day_date")
        price =  dictionary.get("price")
        vacation_pic =  dictionary.get("vacation_pic")
        vacation = CountryModel(vacationId,country,v_description,start_date,last_day_date,price,vacation_pic )
        return vacation



    @staticmethod
    def dictionaries_to_vacations(list_of_dictionary):
        vacations = () 
        for item in list_of_dictionary:
            vacation = CountryModel.dictionary_to_vacation(item)
            vacations.append(vacation)
        return vacations
      