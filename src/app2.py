
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

x=VacationLogic()
result=x.get_vacation_by_country(country="Germany")
for row in result:
    print (row)

