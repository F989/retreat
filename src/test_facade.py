from facades.facade_vacation import *
from facades.user_facade import *
from facades.like_facade import *
from functools import reduce

                                                                                                    
class Test:

    def __init__(self):
        self.user = UserFacade()
        self.vacation = VacationFacade()
        self.like = LikeFacade()
     

    def test_register_to_system(self,):# This is a one time test since there is no delete function to delete addition later on
        self.wrapped_stars_message('Tests for the function: register_to_system')
        print(' test_register_to_system by entering: ')
        print("fname= 'yoni',lname='shlush',Email= 'shlush@gamil.com',Password='joy1'")
        with self.user as user:
            register = user.register_to_system(fname= 'yoni',lname='shlush',Email= 'shlush@gamil.com',Password='joy1' )
            print (register)
        
    def test_character_overflow_in_fname_register_to_system(self,):
        print(' test_character_overflow_in_fname_in_register_to_system by entering: ')
        print(f"fname= '{'Asaf '*12}',lname='shlush',Email= 'shlush@gamil.com',Password='joy1' ")
        with self.user as user:
            register = user.register_to_system(fname= 'Asaf '*12,lname='shlush',Email= 'shlush@gamil.com',Password='joy1' )
            print(register)

    def test_character_overflow_in_lname_register_to_system(self,):
        print(' test_character_overflow_in_lname_in_register_to_system by entering: ')
        print(f"fname = 'shlush',lname=f'{'dumpy '*12}',Email= 'shlush@gamil.com',Password='joy1' ")
        with self.user as user:
            register = user.register_to_system(fname= 'shlush',lname='dumpy '*12,Email= 'shlush@gamil.com',Password='joy1' )
            print(register)


    def test_character_overflow_in_Email_register_to_system(self,):
        print(' test_character_overflow_in_fname_in_register_to_system by entering: ')
        print(f"fname = 'shlush',lname='shlush',Email= '{'Asaf '*12}@gamil.com',Password='joy1' ")
        with self.user as user:
            register = user.register_to_system(fname= 'shlush',lname='shlush',Email= f'{'Asaf '*12}@gamil.com',Password='joy1' )
            print(register)

    def test_character_overflow_in_Password_register_to_system(self,):
        print(' test_character_overflow_in_fname_in_register_to_system by entering: ')
        print(f"fname= 'shlush',lname='shlush',Email= 'joy@gamil.com',Password='{'Asaf '*12}' ")
        with self.user as user:
            register = user.register_to_system(fname= 'shlush',lname='shlush',Email= 'jgamil.com',Password='Asaf '*12 )
            print(register)


    def test_invalid_Email_in_register_to_system(self,):#parameter is not legit
        print (' test_invalid_Email_register_to_system by entering:')
        print( "fname= 'shlush',lname='shlush',Email= 'jgamil.com',Password='joy1'")
        with self.user as user:
            register = user.register_to_system(fname= 'shlush',lname='shlush',Email= 'jgamil.com',Password='joy1' )
            print(register)

    def test_invalid_password_in_register_to_system(self,):#parameter is not legit
        print (' test_invalid_password_in_register_to_system by entering:')
        print( "fname= 'shlush',lname='shlush',Email= 'jfd@gamil.com',Password='123'")
        with self.user as user:
            register = user.register_to_system(fname= 'shlush',lname='shlush',Email= 'jfd@gamil.com',Password='123' )
            print(register)

    def test_type_int_fname_in_register_to_system(self,):#wrong class type parameter
        print (' test_type_int_fname_in_register_to_system by entering:')
        print( "fname= '123pp',lname='shlush',Email= 'jfd@gamil.com',Password='joy1'")
        with self.user as user:
            register = user.register_to_system(fname= '123pp',lname='shlush',Email= 'jfd@gamil.com',Password='joy1' )
            print(register)

    def test_type_int_lname_register_to_system(self,):#wrong class type parameter
        print (' test_type_int_lname_in_register_to_system by entering:')
        print( "fname= 'shlush',lname='123pp',Email= 'jfd@gamil.com',Password='joy1'")
        with self.user as user:
            register = user.register_to_system(fname= 'shlush',lname='123pp',Email= 'jfd@gamil.com',Password='joy1' )
            print(register)     

    def test_empty_fname_input_in_register_to_system(self,):
        print (' test_empty_fname_input_in_register_to_system by entering:')
        print( "fname = '',lname ='poly',Email = 'jfd@gamil.com',Password ='joy1'")
        with self.user as user:
            register = user.register_to_system(fname = '',lname ='poly',Email = 'jfd@gamil.com',Password ='joy1' )
            print(register)

    def test_empty_lname_input_in_register_to_system(self,):
        print (' test_empty_fname_input_in_register_to_system by entering:')
        print( "fname = 'poly',lname ='',Email = 'jfd@gamil.com',Password ='joy1'")
        with self.user as user:
            register = user.register_to_system(fname = 'poly',lname ='',Email = 'jfd@gamil.com',Password = 'joy1' )
            print(register)

    def test_empty_email_input_in_register_to_system(self,):
        print (' test_empty_email_input_in_register_to_system by entering:')
        print( "fname = 'paul',lname ='poly',Email = '',Password ='joy1'")
        with self.user as user:
            register = user.register_to_system(fname = 'paul',lname ='poly',Email = '',Password ='joy1' )
            print(register)

    def test_empty_password_input_in_register_to_system(self,):
        print (' test_empty_password_input_in_register_to_system by entering:')
        print( "fname = 'paul',lname ='poly',Email = 'joy@ghr.com',Password =''")
        with self.user as user:
            register = user.register_to_system(fname = 'paul',lname ='poly',Email = 'joy@ghr.com',Password ='' )
            print(register)

    def all_tests_for_register_to_system(self):# putting all tests of the same function in a list
        return [
        self.test_register_to_system,
        self.test_character_overflow_in_fname_register_to_system,
        self.test_character_overflow_in_lname_register_to_system,
        self.test_character_overflow_in_Email_register_to_system,
        self.test_character_overflow_in_Password_register_to_system,
        self.test_invalid_Email_in_register_to_system,
        self.test_invalid_password_in_register_to_system,
        self.test_type_int_fname_in_register_to_system,
        self.test_type_int_lname_register_to_system,
        self.test_empty_fname_input_in_register_to_system,
        self.test_empty_lname_input_in_register_to_system,
        self.test_empty_email_input_in_register_to_system,
        self.test_empty_password_input_in_register_to_system
        ]

    def test_sign_in_for_registered_users(self):
        self.wrapped_stars_message('tests for the function: sign_in_for_registered_users')
        print(' test_sign_in_for_registered_users with the input: ')
        print("Email= 'shlush@gamil.com',Password='joy1'")
        with self.user as user:
            sign_in = user.sign_in_for_registered_users(Email = 'shlush@gamil.com',Password ='joy1' )
            print (sign_in)

    def test_character_overflow_email_sign_in_for_registered_users(self):
        print(' test_character_overflow_email_sign_in_for_registered_users with the input: ')
        print(f"Email = '{'Ido '*16}@gamil.com@',Password ='joy1'")
        with self.user as user:
            sign_in = user.sign_in_for_registered_users(Email = f'{"ido "*16}@gamil.com',Password ='joy1' )
            print (sign_in)

    def test_character_overflow_password_sign_in_for_registered_users(self):
        print(' test_character_overflow_password_sign_in_for_registered_users with the input: ')
        print(f"Email= 'shlush@gamil.com',Password='{'Elisha '*8}")
        with self.user as user:
            sign_in = user.sign_in_for_registered_users(Email = 'shlush@gamil.com',Password ='Elisha '*8 )
            print (sign_in)

    def test_invalid_email_sign_in_for_registered_users(self):#parameter is not legit
        print (' test_invalid_email_sign_in_for_registered_users by entering:')
        print( "Email = 'jgamil.com', Password = 'joy1' ")
        with self.user as user:
            sign_in = user.sign_in_for_registered_users(Email = 'jgamil.com',Password ='joy1' )
            print(sign_in)
        
    def test_invalid_password_sign_in_for_registered_users(self):#parameter is not legit
        print (' test_invalid_password_sign_in_for_registered_users by entering:')
        print( "Email= 'shlush@gamil.com',Password = '123'")
        with self.user as user:
            sign_in = user.sign_in_for_registered_users(Email = 'shlush@gamil.com',Password='123' )
            print(sign_in)

    def test_unregistered_email_sign_in_for_registered_users(self):#parameter is not in DB
        print (' test_unregistered_email_sign_in_for_registered_user by entering:')
        print( 'Email = porky@jamil.com,Password = joy1')
        with self.user as user:
            sign_in = user.sign_in_for_registered_users(Email= 'porky@jamil.com',Password='joy1' )
            print(sign_in)

    def test_wrong_password_sign_in_for_registered_users(self):#parameter is not in DB
        print (' test_wrong_password_sign_in_for_registered_users by entering:')
        print( 'Email = shlush@gamil.com,Password = skhjhfdkj532')
        with self.user as user:
            sign_in = user.sign_in_for_registered_users(Email = 'shlush@gamil.com',Password ='skhjhfdkj532' )
            print(sign_in)
    def test_empty_email_input_in_sign_in_for_registered_users(self,):
        print (' test_empty_email_input_in_sign_in_for_registered_users by entering:')
        print( "'Email = "",Password = 'joy1'")
        with self.user as user:
            sign_in = user.sign_in_for_registered_users(Email= '',Password='joy1' )
            print(sign_in)

    def test_empty_password_input_in_sign_in_for_registered_users(self,):
        print (' test_empty_password_input_in_sign_in_for_registered_users by entering:')
        print("Email= 'shlush@gamil.com',Password=''")
        with self.user as user:
            sign_in = user.sign_in_for_registered_users(Email= 'shlush@gamil.com',Password='' )
            print(sign_in)

    def all_tests_for_sign_in_for_registered_users(self):
        return [
        self.test_sign_in_for_registered_users,    
        self.test_character_overflow_email_sign_in_for_registered_users,
        self.test_character_overflow_password_sign_in_for_registered_users,
        self.test_invalid_email_sign_in_for_registered_users,
        self.test_invalid_password_sign_in_for_registered_users,
        self.test_unregistered_email_sign_in_for_registered_users,
        self.test_wrong_password_sign_in_for_registered_users,
        self.test_empty_email_input_in_sign_in_for_registered_users,
        self.test_empty_password_input_in_sign_in_for_registered_users
        ]
    
    def test_add_like (self):
        self.wrapped_stars_message('tests for the function: add_like')
        print (" test_add_like by entering: ")
        print("userId = '4',vacationId= '57'")
        with self.like as like:
            add_like = like.add_like(userId = '4',vacationId= '57')#two parameters that are not in the data base
            print(add_like)
         

    def test_add_like_like_already_exists(self):
        print (" test_add_like_like_already_exists by entering: ")
        print("userId = '4',vacationId= '57'")
        with self.like as like:
            add_like = like.add_like(userId = '4',vacationId= '57')#two parameters that are in the data base
            print(add_like)
        

    def test_empty_value_in_userId_in_add_like(self):
        print (" test_empty_value_in_userId_in_add_like by entering: ")
        print("userId = '',vacationId= '60'")
        with self.like as like:
            add_like = like.add_like(userId = '',vacationId= '60')#two parameters that are in the data base
            print(add_like)

    def test_empty_value_in_vacationId_in_add_like(self):
        print (" test_empty_value_in_vacationId_in_add_like by entering: ")
        print("userId = '4',vacationId= ''")
        with self.like as like:
            add_like = like.add_like(userId = '4',vacationId= '')#two parameters that are in the data base
            print(add_like) 

    def test_letters_in_UserId_in_add_like (self):#str when an int type value is demanded
        print (" test_letters_in_UserId_in_add_like by entering: ")
        print("userId = 'abc',vacationId= '60'")
        with self.like as like:
            add_like = like.add_like(userId = 'abc',vacationId= '60')
            print(add_like)

    def test_letters_in_vacationId_add_like (self):#str when an int type value is demanded
        print (" test_letters_in_vacationId_add_like by entering: ")
        print("userId = '4',vacationId= 'abc'")
        with self.like as like:
            add_like = like.add_like(userId = '4',vacationId= 'abc')
            print(add_like)

    def test_wrong_userId_add_like (self):#typing a parameter that does not exist in DB
        print (" test_wrong_userId_add_like by entering: ")
        print("userId = '123',vacationId= '60'")
        with self.like as like:
            add_like = like.add_like(userId = '123',vacationId= '60')#userId not in data base
            print(add_like)

    def test_Wrong_vacationId_add_like (self):#typing a parameter that does not exist in DB
        print (" test_Wrong_vacationId_add_like by entering: ")
        print("userId = '4',vacationId= '123'")
        with self.like as like:
            add_like = like.add_like(userId = '4',vacationId= '123')#vactionId not in data base
            print(add_like)

     
    def all_tests_for_add_like (self):#puts all test of the same function in a list
        return [
        self.test_add_like,
        self.test_add_like_like_already_exists,
        self.test_empty_value_in_userId_in_add_like,
        self.test_empty_value_in_vacationId_in_add_like,
        self.test_letters_in_UserId_in_add_like,
        self.test_letters_in_vacationId_add_like,
        self.test_wrong_userId_add_like,
        self.test_Wrong_vacationId_add_like
        ]

    def test_delete_like(self):
        self.wrapped_stars_message('tests for the function: delete_like')
        print (" test_delete_like by entering: ")
        print("userId = '4',vacationId= '57'")
        with self.like as like:
            delete_like = like.delete_like(userId = '4',vacationId= '57')#two parameters that are in the data base and in like table
            print(delete_like)

    def test_wrong_userId_delete_like(self):#typing a parameter that does not exist in DB
        print (" test_wrong_userId_delete_like by entering: ")
        print("userId = '123',vacationId= '59'")
        with self.like as like:
            delete_like = like.delete_like(userId = '123',vacationId= '59')#userId not in table
            print(delete_like)

    def test_wrong_vacationId_delete_like(self):#typing a parameter that does not exist in DB
        print (" test_wrong_userId_delete_like by entering: ")
        print("userId = '26',vacationId= '34'")
        with self.like as like:
            delete_like = like.delete_like(userId = '26',vacationId= '34')#vacationId not in table
            print(delete_like)

    def test_str_userId_delete_like(self):#wrong class type of character
        print (" test_str_userId_delete_like by entering: ")
        print("userId = 'abc',vacationId= '59'")
        with self.like as like:
            delete_like = like.delete_like(userId = 'abc',vacationId= '59')
            print(delete_like)

    def test_str_vacationId_like_delete_like(self):#wrong class type character
        print (" test_str_vacationId_like_delete_like by entering: ")
        print("userId = '26',vacationId= 'abc'")
        with self.like as like:
            delete_like = like.delete_like(userId = '4',vacationId= 'abc')
            print(delete_like)

    def test_userId_not_in_likes_table_in_delete_like(self):
        print (" test_userId_not_in_likes_table_in_delete_like by entering: ")
        print("userId = '28',vacationId= '69'")
        with self.like as like:
            delete_like = like.delete_like(userId = '28',vacationId= '69')#userId exists but not in likes table unlike vacationId that does
            print(delete_like)

    def test_vacationId_not_in_likes_table_in_delete_like(self):
        print (" test_vacationId_not_in_likes_table_in_delete_like by entering: ")
        print("userId = '26',vacationId= '61'")
        with self.like as like:
            delete_like = like.delete_like(userId = '26',vacationId= '61')#vacationId exists but not in likes table unlike userId that does
            print(delete_like)

    def test_empty_value_in_userId_in_delete_like(self):
        print (" test_empty_value_in_userId_in_delete_like by entering: ")
        print("userId = '',vacationId= '69'")
        with self.like as like:
            delete_like = like.delete_like(userId = '',vacationId= '69')
            print(delete_like)

    def test_empty_value_in_vacationId_in_delete_like(self):
        print (" test_empty_value_in_vacationId_in_delete_like by entering: ")
        print("userId = '26',vacationId= ''")
        with self.like as like:
            delete_like = like.delete_like(userId = '26',vacationId= '')
            print(delete_like)

    def all_tests_for_delete_like(self):#puts all tests of the same function in a list
        return [
        self.test_delete_like,
        self.test_wrong_userId_delete_like,
        self.test_wrong_vacationId_delete_like,
        self.test_str_userId_delete_like,
        self.test_str_vacationId_like_delete_like,
        self.test_userId_not_in_likes_table_in_delete_like,
        self.test_vacationId_not_in_likes_table_in_delete_like,
        self.test_empty_value_in_vacationId_in_delete_like
        ]
    
    def test_get_all_vacation_ordered_by_date(self,):
        self.wrapped_stars_message('tests for the function: get_all_vacation_ordered_by_date')
        print("test 'test_get_all_vacation_ordered_by_date: ' ")
        with self.vacation as vacation:
            all_vacations = vacation.get_all_vacation_ordered_by_date()
            for vacation in all_vacations:
                print (vacation)
    
    def all_tests_for_get_all_vacation_ordered_by_date(self):
        return [self.test_get_all_vacation_ordered_by_date]
    
    def test_create_new_vacation(self,):
        self.wrapped_stars_message('tests for the function: create_new_vacation')
        print("test_create_new_vacation by entering: ")
        print('v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-14",last_day_date="2024-07-17",price="9000",vacation_pic="16.jpg",countryId="6"')
        with self.vacation as vacation:
            create_new =vacation.create_new_vacation(v_description = "5 star hotel,snowy mountain view,half board" ,start_date = "2024-07-14",last_day_date="2024-07-17",price="9000",vacation_pic="16.jpg",countryId="6")
            print(create_new)    
   
    
    def test_create_new_vacation_invalid_start_date(self,):
        print("test_create_new_vacation_invalid_start_date by entering: ")
        print('v_description = "5 star hotel,snowy mountain view,half board" ,start_date = "2024-07-17",last_day_date = "2024-07-14",price="9000",vacation_pic="16.jpg",countryId="6"')
        with self.vacation as vacation:
            create_new =vacation.create_new_vacation(v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-17",last_day_date="2024-07-14",price="9000",vacation_pic="16.jpg",countryId="6")
            print(create_new)

    def test_create_new_vacation_invalid_last_day_date(self,):
        print("test_create_new_vacation_invalid_last_day_date by entering: ")
        print('v_description = "5 star hotel,snowy mountain view,half board" ,start_date = "2024-07-17",last_day_date = "2024/07/14",price="9000",vacation_pic="16.jpg",countryId="6"')
        with self.vacation as vacation:
            create_new =vacation.create_new_vacation(v_description = "5 star hotel,snowy mountain view,half board" ,start_date = "2024-07-17",last_day_date="2024/07/14",price="9000",vacation_pic="16.jpg",countryId="6")
            print(create_new)

    def test_create_new_vacation_over_10000_price(self,):
        print("test_create_new_vacation_over_10000_price")
        print('v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-14",last_day_date="2024-07-17",price="14000",vacation_pic="16.jpg",countryId="6"')
        with self.vacation as vacation:
            create_new =vacation.create_new_vacation(v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-14",last_day_date="2024-07-17",price="14000",vacation_pic="16.jpg",countryId="6")
            print(create_new)    

    def test_create_new_vacation_negative_price(self,):
            print("test_create_new_vacation_negative_price")
            print('v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-14",last_day_date="2024-07-17",price="-3000",vacation_pic="16.jpg",countryId="6"')
            with self.vacation as vacation:
                create_new =vacation.create_new_vacation(v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-14",last_day_date="2024-07-17",price="-3000",vacation_pic="16.jpg",countryId="6")
                print(create_new) 

    def test_create_new_vacation_empty_countryId_field(self,):
        print ("test_create_new_vacation_empty_countryId_field by entering: ")
        print("v_description = 'tree hotel, forest view, full board' or start_date ='2024-10-16' or last_day_date = '2025-04-07' or price = '3000' or countryId = ''")
        with self.vacation as vacation:
            create_new =vacation.create_new_vacation(v_description = 'tree hotel, forest view, full board', start_date = '2024-10-16', last_day_date = '2025-04-07', price = '3000' , countryId = '')
            print(create_new)

    def test_create_new_vacation_empty_price_field(self,):
            print ("test_create_new_vacation_empty_price_field by entering: ")
            print("v_description = 'tree hotel, forest view, full board' or start_date ='2024-10-16' or last_day_date = '2025-04-07' or price = '' or countryId = '6'")
            with self.vacation as vacation:
                create_new =vacation.create_new_vacation(v_description = 'tree hotel, forest view, full board', start_date = '2024-10-16', last_day_date = '2025-04-07', price = '' , countryId = '6')
                print(create_new)

    def test_create_new_vacation_empty_last_day_date_field(self,):
            print ("test_create_new_vacation_empty_last_day_date_field by entering: ")
            print("v_description = 'tree hotel, forest view, full board' or start_date ='2024-10-16' or last_day_date = '' or price = '3000' or countryId = '6'")
            with self.vacation as vacation:
                create_new =vacation.create_new_vacation(v_description = 'tree hotel, forest view, full board', start_date = '2024-10-16', last_day_date = '', price = '3000' , countryId = '6')
                print(create_new)
    
    def test_create_new_vacation_empty_start_date_field(self,):
            print ("test_create_new_vacation_empty_start_date_field by entering: ")
            print("v_description = 'tree hotel, forest view, full board' or start_date ='' or last_day_date = '2025-04-07' or price = '3000' or countryId = '6'")
            with self.vacation as vacation:
                create_new =vacation.create_new_vacation(v_description = 'tree hotel, forest view, full board', start_date = '', last_day_date = '2025-04-07', price = '3000' , countryId = '6')
                print(create_new)

    def test_create_new_vacation_empty_v_description_field(self,):
            print ("test_create_new_vacation_empty_v_description_field")
            print("v_description ='' or start_date ='2024-10-16' or last_day_date = '2025-04-07' or price = '' or countryId = '6'")
            with self.vacation as vacation:
                create_new =vacation.create_new_vacation(v_description = '', start_date = '2024-10-16', last_day_date = '2025-04-07', price = '3000' , countryId = '6')
                print(create_new)
          

    def test_create_new_vacation_price_pattern_not_valid(self,):
        print("test_create_new_vacation_price_pattern_not_valid  by entering: ")
        print('v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-14",last_day_date="2024-07-17",price="140@g*",vacation_pic="16.jpg",countryId="6"')
        with self.vacation as vacation:
            create_new =vacation.create_new_vacation(v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-14",last_day_date="2024-07-17",price="140@g*",vacation_pic="16.jpg",countryId="6")
            print(create_new)

    def test_create_new_vacation_incorrect_start_date_pattern(self,) :
        print("test incorrect date pattern date= start_date by entering: ")
        print('v_description="5 star hotel,snowy mountain view,half board" ,start_date="20-0724-145",last_day_date="20-0247-187",price="9000",vacation_pic="16.jpg",countryId="6"')
        with self.vacation as vacation:
            create_new =vacation.create_new_vacation(v_description="5 star hotel,snowy mountain view,half board" ,start_date="20-0724-145",last_day_date="20-0247-187",price="9000",vacation_pic="16.jpg",countryId="6")
            print(create_new)     

    def test_create_new_vacation_incorrect_last_day_date_pattern(self,) :
        print("test_create_new_vacation_incorrect_last_day_date_pattern by entering: ")
        print('v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-14",last_day_date="20-0247-187",price="9000",vacation_pic="16.jpg",countryId="6"')
        with self.vacation as vacation:
            create_new =vacation.create_new_vacation(v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-14",last_day_date="20-0247-187",price="9000",vacation_pic="16.jpg",countryId="6")
            print(create_new)      
    

    def test_create_new_vacation_countryId_is_not_integer(self,):
        print("test_create_new_vacation_countryId_is_not_integer by entering:")
        print('v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-14",last_day_date="2024-07-17",price="9000",vacation_pic="16.jpg",countryId="abc"')
        with self.vacation as vacation:
            create_new =vacation.create_new_vacation(v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-14",last_day_date="2024-07-17",price="9000",vacation_pic="16.jpg",countryId="abc")
            print(create_new)   


    def test_create_new_vacation_countryId_does_not_exist(self,):
        print("test_create_new_vacation_countryId_does_not_exist by entering: ")
        print( 'v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-14",last_day_date="2024-07-17",price="9000",vacation_pic="16.jpg",countryId="45"')
        with self.vacation as vacation:
            create_new =vacation.create_new_vacation(v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-14",last_day_date="2024-07-17",price="9000",vacation_pic="16.jpg",countryId="45")
            print(create_new)   

    def test_create_new_vacation_arrival_after_departure(self):
        print('test_create_new_vacation_arrival_after_departure by entering: ')
        print( 'v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-10-14",last_day_date="2024-07-17",price="9000",vacation_pic="16.jpg",countryId="45"')
        with self.vacation as vacation:
            create_new =vacation.create_new_vacation(v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-10-14",last_day_date="2024-07-17",price="9000",vacation_pic="16.jpg",countryId="45")
            print(create_new)   

    def test_create_new_vacation_v_description_overflow(self,):
        print("test_create_new_vacation_v_description_overflow by entering: ")
        print(f'v_description="{'lisa'*64}" ,start_date="2024-07-14",last_day_date="2024-07-17",price="9000",vacation_pic="16.jpg",countryId="6"')
        with self.vacation as vacation:
            create_new =vacation.create_new_vacation(v_description = "lisa"*64 ,start_date = "2024-07-14",last_day_date="2024-07-17",price="9000",vacation_pic="16.jpg",countryId="6")
            print(create_new)  

    def test_create_new_vacation_vacation_pic_overflow(self,):
        print("test_create_new_vacation_v_description_overflow by entering: ")
        print(f'v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-14",last_day_date="2024-07-17",price="9000",vacation_pic="{'Ido.Elisha '*26}",countryId="6"')
        with self.vacation as vacation:
            create_new =vacation.create_new_vacation(v_description = "5 star hotel,snowy mountain view,half board" ,start_date = "2024-07-14",last_day_date="2024-07-17",price="9000",vacation_pic="Ido.Elisha "*300,countryId="6")
            print(create_new) 
    
    
    def all_tests_for_create_new_vacation(self):
        return [
        self.test_create_new_vacation,
        self.test_create_new_vacation_invalid_start_date,
        self.test_create_new_vacation_invalid_last_day_date,
        self.test_create_new_vacation_over_10000_price,
        self.test_create_new_vacation_negative_price,
        self.test_create_new_vacation_empty_countryId_field,
        self.test_create_new_vacation_empty_price_field,
        self.test_create_new_vacation_empty_last_day_date_field,
        self.test_create_new_vacation_empty_start_date_field,
        self.test_create_new_vacation_empty_v_description_field,
        self.test_create_new_vacation_price_pattern_not_valid,
        self.test_create_new_vacation_incorrect_start_date_pattern,
        self.test_create_new_vacation_incorrect_last_day_date_pattern,
        self.test_create_new_vacation_countryId_is_not_integer,
        self.test_create_new_vacation_countryId_does_not_exist,
        self.test_create_new_vacation_arrival_after_departure,
        self.test_create_new_vacation_v_description_overflow,
        self.test_create_new_vacation_vacation_pic_overflow
        ]


    def test_update_vacation(self):
        self.wrapped_stars_message('tests for the function: update_vacation')
        print("test_update_vacation by entering: ")
        print('vacationId = "66" ,v_description = "5 star hotel,snowy mountain view,half board" ,start_date = "2024-07-17",last_day_date = "2024-10-14",price = "7000",vacation_pic = "16.jpg",countryId = "6"')
        with self.vacation as vacation:
            update_v = vacation.update_vacation(vacationId = "66" ,v_description = "5 star hotel,snowy mountain view,half board" ,start_date = "2024-07-17",last_day_date = "2024-10-14",price = "7000",vacation_pic = "16.jpg",countryId="6")
            print(update_v) 


    def test_update_vacation_invalid_start_date(self,):
        print("test_update_vacation_invalid_start_date by entering: ")
        print('vacationId = "66" ,v_description = "5 star hotel,snowy mountain view,half board" ,start_date = "202gjhg07-17",last_day_date = "2024-07-14",price="9000",vacation_pic="16.jpg",countryId="6"')
        with self.vacation as vacation:
            update =vacation.update_vacation(vacationId = "66" ,v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-17",last_day_date="2024-07-14",price="9000",vacation_pic="16.jpg",countryId="6")
            print(update)

    def test_update_vacation_invalid_last_day_date(self,):
        print("test_update_vacation_invalid_last_day_date by entering: ")
        print('vacationId = "66" ,v_description = "5 star hotel,snowy mountain view,half board" ,start_date = "2024-07-17",last_day_date = "2024/07/14",price="9000",vacation_pic="16.jpg",countryId="6"')
        with self.vacation as vacation:
            update = vacation.update_vacation(vacationId = "66" ,v_description = "5 star hotel,snowy mountain view,half board" ,start_date = "2024-07-17",last_day_date="2024/07/14",price="9000",vacation_pic="16.jpg",countryId="6")
            print(update)

    def test_update_vacation_over_10000_price(self,):
        print("test_update_vacation_over_10000_price by entering: ")
        print('vacationId = "66" ,v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-14",last_day_date="2024-07-17",price="14000",vacation_pic="16.jpg",countryId="6"')
        with self.vacation as vacation:
            update =vacation.update_vacation(vacationId = "66" ,v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-14",last_day_date="2024-07-17",price="14000",vacation_pic="16.jpg",countryId="6")
            print(update)   
    
    def test_update_vacation_negative_price(self,):
            print("test_update_vacation_negative_price")
            print('v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-14",last_day_date="2024-07-17",price="-3000",vacation_pic="16.jpg",countryId="6"')
            with self.vacation as vacation:
                update = vacation.update_vacation(v_description ="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-14",last_day_date="2024-07-17",price="-3000",vacation_pic="16.jpg",countryId="6")
                print(update) 

    def test_update_vacation_empty_vacationId(self,):
            print("test_update_vacation_empty_vacationId by entering: ")
            print('vacationId = "" ,v_description = "5 star hotel,snowy mountain view,half board" ,start_date = "2024-07-17",last_day_date = "2024-10-14",price = "7000",vacation_pic = "16.jpg",countryId = "6"')
            with self.vacation as vacation:
                update_v = vacation.update_vacation(vacationId = "" ,v_description = "5 star hotel,snowy mountain view,half board" ,start_date = "2024-07-17",last_day_date = "2024-10-14",price = "7000",vacation_pic = "16.jpg",countryId="6")
                print(update_v) 

    def test_update_vacation_all_update_fields_are_empty(self,):
        print ("test_update_vacation_all_fields_are_empty by entering: ")
        print("vacationId = '66' ,v_description = '' or start_date ='' or last_day_date = '' or price = '' or countryId = ''")
        with self.vacation as vacation:
            update =vacation.update_vacation(vacationId = "66" ,v_description = '', start_date = '', last_day_date = '', price = '' , countryId = '')
            print(update)

    def test_update_vacation_countryId_is_not_integer(self,):
        print("test_update_vacation_countryId_is_not_integer by entering:")
        print('vacationId = "66" ,v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-14",last_day_date="2024-07-17",price="9000",vacation_pic="16.jpg",countryId="abc"')
        with self.vacation as vacation:
            update =vacation.update_vacation(vacationId = "66" ,v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-14",last_day_date="2024-07-17",price="9000",vacation_pic="16.jpg",countryId="abc")
            print(update)  

    def test_update_vacation_arrival_after_departure(self):
            print('test_update_vacation_arrival_after_departure by entering: ')
            print( 'vacationId = "66" ,v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-10-14",last_day_date="2024-07-17",price="9000",vacation_pic="16.jpg",countryId="45"')
            with self.vacation as vacation:
                update =vacation.update_vacation(vacationId = "66" ,v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-10-14",last_day_date="2024-07-17",price="9000",vacation_pic="16.jpg",countryId="45")
                print(update)  

    def test_update_vacation_vacationId_is_not_integer(self):
        print("test_update_vacation_vacationId_is_not_integer by entering:")
        print('vacationId = "abc" ,v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-14",last_day_date="2024-07-17",price="9000",vacation_pic="16.jpg",countryId="abc"')
        with self.vacation as vacation:
            update =vacation.update_vacation(vacationId = "abc" ,v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-14",last_day_date="2024-07-17",price="9000",vacation_pic="16.jpg",countryId="6")
            print(update)  

    def test_update_vacation_vacationId_is_not_in_system(self):
        print("test_update_vacation_vacationId_not_in_system by entering:")
        print('vacationId = "107" ,v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-14",last_day_date="2024-07-17",price="9000",vacation_pic="16.jpg",countryId="abc"')
        with self.vacation as vacation:
            update =vacation.update_vacation(vacationId = "107" ,v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-14",last_day_date="2024-07-17",price="9000",vacation_pic="16.jpg",countryId="6")
            print(update)

    def test_update_vacation_countryId_does_not_exist(self,):
        print("test_update_vacation_countryId_does_not_exist by entering: ")
        print( 'vacationId = "66" ,v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-14",last_day_date="2024-07-17",price="9000",vacation_pic="16.jpg",countryId="45"')
        with self.vacation as vacation:
            update =vacation.update_vacation(vacationId = "66" ,v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-14",last_day_date="2024-07-17",price="9000",vacation_pic="16.jpg",countryId="45")
            print(update)  

    def test_update_vacation_price_pattern_not_valid(self,):
            print("test_update_vacation_price_pattern_not_valid  by entering: ")
            print('v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-14",last_day_date="2024-07-17",price="140@g*",vacation_pic="16.jpg",countryId="6"')
            with self.vacation as vacation:
                update =vacation.update_vacation(v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-14",last_day_date="2024-07-17",price="140@g*",vacation_pic="16.jpg",countryId="6")
                print(update)

    def test_update_vacation_v_description_overflow(self,):
        print("test_update_vacation_v_description_overflow by entering: ")
        print(f'v_description="{'AsafAmir '*32}" ,start_date = "2024-07-14",last_day_date = "2024-07-17",price = "9000",vacation_pic = "16.jpg",countryId = "6"')
        with self.vacation as vacation:
            update = vacation.update_vacation(v_description = "AsafAmir"*32 ,start_date = "2024-07-14",last_day_date="2024-07-17",price="9000",vacation_pic="16.jpg",countryId="6")
            print(update)  

    def test_update_vacation_vacation_pic_overflow(self,):
        print("test_update_vacation_v_description_overflow by entering: ")
        print(f'v_description="5 star hotel,snowy mountain view,half board" ,start_date = "2024-07-14",last_day_date="2024-07-17",price = "9000",vacation_pic = "{'Asaf.Amir'*29}",countryId = "6"')
        with self.vacation as vacation:
            update = vacation.update_vacation(v_description = "5 star hotel,snowy mountain view,half board" ,start_date = "2024-07-14",last_day_date = "2024-07-17",price = "9000",vacation_pic = 'Asaf.Amir'*29,countryId = "6")
            print(update) 



    def all_tests_for_update_vacation(self):
        return [
        self.test_update_vacation,
        self.test_update_vacation_invalid_start_date,
        self.test_update_vacation_invalid_last_day_date,
        self.test_update_vacation_all_update_fields_are_empty,
        self.test_update_vacation_countryId_is_not_integer,
        self.test_update_vacation_over_10000_price,
        self.test_update_vacation_negative_price ,
        self.test_update_vacation_arrival_after_departure,
        self.test_update_vacation_vacationId_is_not_integer,
        self.test_update_vacation_empty_vacationId,
        self.test_update_vacation_vacationId_is_not_in_system,
        self.test_update_vacation_countryId_does_not_exist,
        self.test_update_vacation_price_pattern_not_valid,
        self.test_update_vacation_v_description_overflow,
        self.test_update_vacation_vacation_pic_overflow
        ]

    def test_delete_vacation(self):
        self.wrapped_stars_message('tests for the function: delete_vacation')
        print("test_delete_vacation by entering: ")
        print('vacationId = "66"')
        with self.vacation as vacation:
            deletion = vacation.delete_vacation(vacationId = "66")
            print(deletion)
  
    def test_delete_vacation_empty_vacationId(self):
        print("test_delete_vacation_empty_vacationId by entering: ")
        print('vacationId = ""')
        with self.vacation as vacation:
            deletion = vacation.delete_vacation(vacationId = "")
            print(deletion)

    def test_delete_vacation_vacationId_not_in_system(self):
        print("test_delete_vacation_vacationId_not_in_system by entering: ")
        print('vacationId = "4"')#entering a variable that does not exist in the data base
        with self.vacation as vacation:
            deletion = vacation.delete_vacation(vacationId = "4")
            print(deletion)

    
    def test_delete_vacation_vacationId_not_integer(self):
        print("test_delete_vacation_vacationId_not_integer by entering: ")
        print('vacationId = "abc"')#entering a variable that does not exist in the data base
        with self.vacation as vacation:
            deletion = vacation.delete_vacation(vacationId = "abc")
            print(deletion)

    def all_tests_for_delete_vacation(self):#putting all test functions of the same function in a list
            return [
            self.test_delete_vacation,
            self.test_delete_vacation_empty_vacationId,
            self.test_delete_vacation_vacationId_not_in_system,
            self.test_delete_vacation_vacationId_not_integer                       
            ]


    def turn_on_all_tests(self):
        list = [              #list of lists of tests of functions
            self.all_tests_for_add_like(),
            self.all_tests_for_delete_like(),
            self.all_tests_for_register_to_system(),
            self.all_tests_for_sign_in_for_registered_users(),
            self.all_tests_for_get_all_vacation_ordered_by_date(),
            self.all_tests_for_create_new_vacation(),
            self.all_tests_for_update_vacation(),
            self.all_tests_for_delete_vacation()
            ] 
        #reduce is a function that allows manipulation on members of list with a function (in this case addition of lists) reduce(function,list)
        list = reduce(self.conc,list)#concatenating 'lists of functions' in list to one list of functions
        for func in list: #pulling each function in list and activating it
            try:
                self.user = UserFacade()
                self.vacation = VacationFacade()        #renewal of instance is needed for each function for stable sql connection
                self.like = LikeFacade()
                func()
            except ValueError as err:
                print("ValueError in vacation_functions tests: ", err)
            except OverflowError as err:
                print("OverflowError in vacation_functions tests: ", err)
            except TypeError as err:
                print("TypeError in vacation_functions tests: ", err)
            except Exception as err:
                print("Error in vacation_functions tests: ", err)
            finally: 
                print("----------------Test over--------------------")
        self.wrapped_stars_message('All tests completed')
        print('Side note: we also made an exception for the connection error, you can see it in the dal module.\n \n Have a great day.')
        
        

    def conc(self,x,y):# a function for concatenating lists in the code(look for 'def turn_on_all_tests' (down at the end of the code))
        return x+y  

    def wrapped_stars_message(self,message):# for cosmetic and better understanding the output
        print()
        for hight in range(3):
            if hight == 0  or hight == 2:
                print("*"*(len(str(message))+4))
            elif 0 < hight < 2:
                print("* " + message + " *")
        print()