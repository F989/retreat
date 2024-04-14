
from logic.logic_vacation import *
from logic.logic_user import *


'''
d = DAL()
sql = "select * from retreat.vacations limit 5 " 
dict_results = d.get_table(sql) 
table = VacationModel.dictionaries_to_vacations(dict_results)
for row in table:
    print(row)
# print(obj_results,)
'''

'''
x = UserLogic()
y= x.insert_user('bor','bgn','aaa@gmail.com','222',2 )
print(y)
d.close()

# x = UserLogic.delete_user(2)


'''
'''
x = VacationLogic()
result = x.get_all_vacations()
for row in result:
    print (row)
'''
# y = VacationLogic()
# result = y.create_new_vacation("5 star hotel,snowy mountain view,half board" ,"2024-07-17","2024-07-14","14000","16.jpg","6")
# print(result)



# z = VacationLogic()
# result = z.update_vacation()
# print(result) 

# x=VacationLogic()
# result=x.get_vacation_by_country(country="Germany")
# for row in result:
#     print (row)

# p=VacationLogic()
# result=p.get_vacation_by_price(price="15000")
# for vacation in result:
#  print (vacation)

# up = VacationLogic()
# result = up.update_vacation_price(price="4000",vacationId="57")
# print(result) 
'''
d=VacationLogic()
result=d.get_vacation_by_date(vacationId="",start_date="", last_day_date="")
for vacation in result:
  print (vacation)
'''
# ud = VacationLogic()
# result = ud.update_vacation_date(start_date="2024-06-02", last_day_date="2024-06-09",vacationId="57")
# print(result) 