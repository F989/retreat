
class VacationModel :

    def __init__(self,vacationId,countryId,v_description,start_date,last_day_date,price,vacation_pic):
     
            self.vacationId = vacationId
            self.countryId = countryId
            self.v_description = v_description
            self.start_date = start_date
            self.last_day_date = last_day_date
            self.price = price
            self.vacation_pic = vacation_pic

    def __str__(self):
         return  (f"vacationId: {self.vacationId} countryId:{self.countryId } v_description:{self.v_description} self.start_date:{self.start_date} "
                f"last_day_date: {self.last_day_date} price:{self.price} vacation_pic:{ self.vacation_pic} " )

    
    @staticmethod
    def dictionary_to_vacation(dictionary):
        vacationId = dictionary["vacationId"]
        countryId =  dictionary["countryId"]
        v_description =  dictionary["v_description"]
        start_date =  dictionary["start_date"]
        last_day_date =  dictionary["last_day_date"]
        price =  dictionary["price"]
        vacation_pic =  dictionary["vacation_pic"]
        vacation = VacationModel(vacationId,countryId,v_description,start_date,last_day_date,price,vacation_pic )
        return vacation



    @staticmethod
    def dictionaries_to_vacations(list_of_dictionary):
        vacations = [] 
        for item in list_of_dictionary:
            vacation = VacationModel.dictionary_to_vacation(item)
            vacations.append(vacation)
        return vacations
   