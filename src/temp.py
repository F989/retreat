from facades.facade_vacation import *
from facades.user_facade import *
from facades.like_facade import *

class Test:

    def __init__(self):
            
            self.vacation = VacationFacade()
            self.user = UserFacade()
            self.like = LikeFacade()
        
  
    def test_get_all_vacations(self):
        print("get all vacation")
        with self.vacation as vacation:
            all_vacations = vacation.get_all_vacations()
        print (all_vacations)
        
    
    def test_create_new_vacation(self):
        print("5 star hotel,snowy mountain view,half board" ,"2024-07-17","2024-07-14","14000","16.jpg","6")
        with self.vacation as vacation:
            create_new =vacation.create_new_vacation(v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-17",last_day_date="2024-07-14",price="14000",vacation_pic="16.jpg",countryId="6")
        print(create_new)

    def test_update_vacation(self,):
        print("5 star hotel,snowy mountain view,half board" ,"2024-07-17","2024-07-14","14000","16.jpg","6")
        with self.vacation as vacation:
         update_v= vacation.update_vacation(v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-17",last_day_date="2024-07-14",price="14000",vacation_pic="16.jpg",countryId="6")
        print(update_v) 
    

    def test_update_vacation_with_invalid_description(self):
        print("Updating vacation with invalid description...")
        with self.vacation as vacation:
            vacation_logic = VacationLogic()
            invalid_description = ""
        try:
            update_result = vacation_logic.update_vacation(v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-17",last_day_date="2024-07-14",price="14000",vacation_pic="16.jpg",countryId="6")
            print(update_result)
        except Exception as e:
            print(f"Invalid description error: {e}")

    def test_update_vacation_with_invalid_start_date(self):
        print("Updating vacation with invalid start date...")
        with self.vacation as vacation:
            # vacation_logic = VacationLogic()
            invalid_start_date = "2024-07-14"
            try:
                update_result = vacation.update_vacation(v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-17",last_day_date="2024-07-14",price="14000",vacation_pic="16.jpg",countryId="6")
                print(update_result)
            except Exception as e:
                print(f"Invalid start date error: {e}")

    def test_update_vacation_with_invalid_price(self):
        print("Updating vacation with invalid price...")
        with self.vacation as vacation:
            vacation_logic = VacationLogic()
            invalid_price = "-14000"
            try:
                update_result = vacation_logic.update_vacation(v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-17",last_day_date="2024-07-14",price="14000",vacation_pic="16.jpg",countryId="6")
                print(update_result)
            except Exception as e:
                print(f"Invalid price error: {e}")

    def test_update_vacation_with_invalid_country_id(self):
        print("Updating vacation with invalid country ID...")
        with self.vacation as vacation:
            vacation_logic = VacationLogic()
            invalid_country_id = "9999" 
            try:
                update_result = vacation_logic.update_vacation(v_description="5 star hotel,snowy mountain view,half board" ,start_date="2024-07-17",last_day_date="2024-07-14",price="14000",vacation_pic="16.jpg",countryId="6")
                print(update_result)
            except Exception as e:
                print(f"Invalid country ID error: {e}")


    def test_delete_vacation(self,):
        print("delete vacation")
        with self.vacation as vacation:
            delete_vacations = vacation.delete_vacation()
            print (delete_vacations)
  
    def test_get_all_vacations_by_date(self):
        print( "start_date =2024-05-04 last_day_date =2024-05-18" ) 
        with self.vacation as vacation:
           
            get_all = vacation.get_all_vacations_by_date(start_date ="2024-05-04" ,last_day_date ="2024-05-18")
            print(get_all)
    
    def test_get_future_vacations(self,):
        print("start_date=2024-05-04,last_day_date=2024-05-18,vacationId=58")
        with self.vacation as vacation:
            get_future=vacation.get_future_vacations(start_date="2024-05-04",last_day_date="2024-05-18",vacationId="58")
        print (get_future)

    def test_update_vacation_date(self,):
        print("start_date=2024-06-02,last_day_date=2024-06-09,vacationId=57")
        with self.vacation as vacation:
        
         update_d= vacation.update_vacation_date(start_date="2024-06-02", last_day_date="2024-06-09",vacationId="57")
        print(update_d) 
    
    def test_Start_date_is_before_last_day_date(self,):
        print("test start date must be before last day date" )
        print("start_date=2024-06-02,last_day_date=2024-06-09,vacationId=57")
        with self.vacation as vacation:
            #
            update_d= vacation.update_(start_date="2024-06-02", last_day_date="2024-06-09",vacationId="57")
        print(update_d) 

    def test_incorrect_date_pattern(self,) : 
        print("start date pattern must be YYYY-MM-DD ")
        print("departure date pattern must be YYYY-MM-DD ")
        print('VacationId=999 is not in the system')
        with self.vacation as vacation:
            update_d= vacation.update_vacation_date(start_date="2024-06-02", last_day_date="2024-06-09",vacationId="999")
        print(update_d) 
    
    # def incorrect_date_pattern(last_day_date) : 
            
    # def vacationId_not_in_system(vacationId):
        print('Vacation not in system')

    def test_vacationId_not_in_system(self,):
        print("vacationId=57")
        with self.vacation as vacation:
        
         not_in=vacation.vacationId_not_in_system(vacationId="57")
        print(not_in)

    def all_tests_for_vacation_functions(self,):
        self.test_get_all_vacations()
        self.test_create_new_vacation()
        self.test_update_vacation()
        self.test_delete_vacation()
        self.test_get_all_vacations_by_date()
        self.test_get_future_vacations()
        self.test_update_vacation_date()
        self.test_vacationId_not_in_system()

    def test_register_to_system(self,):
        print('test_register_to_system with the input: ')
        print("fname= 'yoni',lname='shlush',Email= 'shlush@gamil.com',Password='joy1'")
        with self.user as user:
            register = user.register_to_system(fname= 'yoni',lname='shlush',Email= 'shlush@gamil.com',Password='joy1' )
            print (register)
        
    def test_character_overflow_in_fname_register_to_system(self,):
        print('test_character_overflow_in_fname_in_register_to_system by entering: ')
        print("fname= 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',lname='shlush',Email= 'shlush@gamil.com',Password='joy1' ")
        with self.user as user:
            register = user.register_to_system(fname= 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',lname='shlush',Email= 'shlush@gamil.com',Password='joy1' )
            print(register)

    def test_character_overflow_in_lname_register_to_system(self,):
        print('test_character_overflow_in_lname_in_register_to_system by entering: ')
        print("fname = 'shlush',lname='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',Email= 'shlush@gamil.com',Password='joy1' ")
        with self.user as user:
            register = user.register_to_system(fname= 'shlush',lname='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',Email= 'shlush@gamil.com',Password='joy1' )
            print(register)


    def test_character_overflow_in_Email_register_to_system(self,):
        print('test_character_overflow_in_fname_in_register_to_system by entering: ')
        print("fname = 'shlush',lname='shlush',Email= 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@gamil.com',Password='joy1' ")
        with self.user as user:
            register = user.register_to_system(fname= 'shlush',lname='shlush',Email= 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@gamil.com',Password='joy1' )
            print(register)

    def test_character_overflow_in_Password_register_to_system(self,):
        print('test_character_overflow_in_fname_in_register_to_system by entering: ')
        print("fname= 'shlush',lname='shlush',Email= 'joy@gamil.com',Password='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz1' ")
        with self.user as user:
            register = user.register_to_system(fname= 'shlush',lname='shlush',Email= 'jgamil.com',Password='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz1' )
            print(register)


    def test_invalid_Email_in_register_to_system(self,):#parameter is not legit
        print ('test_invalid_Email_register_to_system by entering:')
        print( "fname= 'shlush',lname='shlush',Email= 'jgamil.com',Password='joy1'")
        with self.user as user:
            register = user.register_to_system(fname= 'shlush',lname='shlush',Email= 'jgamil.com',Password='joy1' )
            print(register)

    def test_invalid_password_in_register_to_system(self,):#parameter is not legit
        print ('test_invalid_password_in_register_to_system by entering:')
        print( "fname= 'shlush',lname='shlush',Email= 'jfd@gamil.com',Password='123'")
        with self.user as user:
            register = user.register_to_system(fname= 'shlush',lname='shlush',Email= 'jfd@gamil.com',Password='123' )
            print(register)

    def test_type_int_fname_in_register_to_system(self,):#wrong class type parameter
        print ('test_type_int_fname_in_register_to_system by entering:')
        print( "fname= '123pp',lname='shlush',Email= 'jfd@gamil.com',Password='joy1'")
        with self.user as user:
            register = user.register_to_system(fname= '123pp',lname='shlush',Email= 'jfd@gamil.com',Password='joy1' )
            print(register)

    def test_type_int_lname_register_to_system(self,):#wrong class type parameter
        print ('test_type_int_lname_in_register_to_system by entering:')
        print( "fname= 'shlush',lname='123pp',Email= 'jfd@gamil.com',Password='joy1'")
        with self.user as user:
            register = user.register_to_system(fname= 'shlush',lname='123pp',Email= 'jfd@gamil.com',Password='joy1' )
            print(register)     

    def test_empty_fname_input_in_register_to_system(self,):
        print ('test_empty_fname_input_in_register_to_system by entering:')
        print( "fname= '',lname='poly',Email= 'jfd@gamil.com',Password='joy1'")
        with self.user as user:
            register = user.register_to_system(fname= '',lname='poly',Email= 'jfd@gamil.com',Password='joy1' )
            print(register)

    def test_empty_lname_input_in_register_to_system(self,):
        print ('test_empty_fname_input_in_register_to_system by entering:')
        print( "fname= 'poly',lname='',Email= 'jfd@gamil.com',Password='joy1'")
        with self.user as user:
            register = user.register_to_system(fname= 'poly',lname='',Email= 'jfd@gamil.com',Password='joy1' )
            print(register)

    def test_empty_email_input_in_register_to_system(self,):
        print ('test_empty_email_input_in_register_to_system by entering:')
        print( "fname= 'paul',lname='poly',Email= '',Password='joy1'")
        with self.user as user:
            register = user.register_to_system(fname= 'paul',lname='poly',Email= '',Password='joy1' )
            print(register)

    def test_empty_password_input_in_register_to_system(self,):
        print ('test_empty_password_input_in_register_to_system by entering:')
        print( "fname= 'paul',lname='poly',Email= 'joy@ghr.com',Password=''")
        with self.user as user:
            register = user.register_to_system(fname= 'paul',lname='poly',Email= 'joy@ghr.com',Password='' )
            print(register)

    def all_tests_for_register_to_system(self,):
        self.test_register_to_system()
        self.test_character_overflow_in_fname_register_to_system()
        self.test_character_overflow_in_lname_register_to_system()
        self.test_character_overflow_in_Email_register_to_system()
        self.test_character_overflow_in_Password_register_to_system
        self.test_invalid_Email_in_register_to_system
        self.test_invalid_password_in_register_to_system
        self.test_type_int_fname_in_register_to_system
        self.test_type_int_lname_register_to_system
        self.test_empty_fname_input_in_register_to_system
        self.test_empty_lname_input_in_register_to_system
        self.test_empty_email_input_in_register_to_system
        self.test_empty_password_input_in_register_to_system


    def test_sign_in_for_registered_users(self):
        print('test_sign_in_for_registered_users with the input: ')
        print("Email= 'shlush@gamil.com',Password='joy1'")
        with self.user as user:
            sign_in = user.sign_in_for_registered_users(self,Email= 'shlush@gamil.com',Password='joy1' )
            print (sign_in)

    def test_character_overflow_email_sign_in_for_registered_users(self):
        print('test_character_overflow_email_sign_in_for_registered_users with the input: ')
        print("Email= 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@gamil.com@',Password='joy1'")
        with self.user as user:
            sign_in = user.sign_in_for_registered_users(self,Email= 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@gamil.com',Password='joy1' )
            print (sign_in)

    def test_character_overflow_password_sign_in_for_registered_users(self):
        print('test_character_overflow_password_sign_in_for_registered_users with the input: ')
        print("Email= 'shlush@gamil.com',Password='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzjoy1'")
        with self.user as user:
            sign_in = user.sign_in_for_registered_users(self,Email= 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@gamil.com',Password='joy1' )
            print (sign_in)

    def test_invalid_email_sign_in_for_registered_users(self):#parameter is not legit
        print ('test_invalid_email_sign_in_for_registered_users by entering:')
        print( "Email = 'jgamil.com', Password = 'joy1' ")
        with self.user as user:
            sign_in = user.sign_in_for_registered_users(Email= 'jgamil.com',Password='joy1' )
            print(sign_in)
        
    def test_invalid_password_sign_in_for_registered_users(self):#parameter is not legit
        print ('test_invalid_password_sign_in_for_registered_users by entering:')
        print( "Email= 'shlush@gamil.com',Password = '123'")
        with self.user as user:
            sign_in = user.sign_in_for_registered_users(Email= 'shlush@gamil.com',Password='123' )
            print(sign_in)

    def test_unregistered_email_sign_in_for_registered_users(self):#parameter is not in DB
        print ('test_unregistered_email_sign_in_for_registered_user by entering:')
        print( 'Email= porky@jamil.com,Password=joy1')
        with self.user as user:
            sign_in = user.sign_in_for_registered_users(Email= 'porky@jamil.com',Password='joy1' )
            print(sign_in)

    def test_wrong_password_sign_in_for_registered_users(self):#parameter is not in DB
        print ('test_wrong_password_sign_in_for_registered_users by entering:')
        print( 'Email= shlush@gamil.com,Password=skhjhfdkj532')
        with self.user as user:
            sign_in = user.sign_in_for_registered_users(Email= 'porky@jamil.com',Password='joy1' )
            print(sign_in)
    def test_empty_email_input_in_sign_in_for_registered_users(self,):
        print ('test_empty_email_input_in_sign_in_for_registered_users by entering:')
        print( "'Email = "",Password='joy1'")
        with self.user as user:
            sign_in = user.sign_in_for_registered_users(Email= '',Password='joy1' )
            print(sign_in)

    def test_empty_password_input_in_sign_in_for_registered_users(self,):
        print ('test_empty_email_input_in_sign_in_for_registered_users by entering:')
        print("Email= 'shlush@gamil.com',Password=''")
        with self.user as user:
            sign_in = user.sign_in_for_registered_users(Email= 'shlush@gamil.com',Password='' )
            print(sign_in)

    def all_tests_for_sign_in_for_registered_users(self):
        self.test_sign_in_for_registered_users()    
        self.test_character_overflow_email_sign_in_for_registered_users()
        self.test_character_overflow_password_sign_in_for_registered_users()
        self.test_invalid_email_sign_in_for_registered_users()
        self.test_invalid_password_sign_in_for_registered_users()
        self.test_unregistered_email_sign_in_for_registered_users()
        self.test_wrong_password_sign_in_for_registered_users()
        self.test_empty_email_input_in_sign_in_for_registered_users()
        self.test_empty_password_input_in_sign_in_for_registered_users()

    def test_add_like (self):
        print ("test_add_like by entering: ")
        print("userId = '4',vacationId= '60'")
        with self.like as like:
            add_like = like.add_like(userId = '4',vacationId= '60')#two parameters that are in the data base
            print(add_like)

    def test_empty_value_in_userId_in_add_like(self):
        print ("test_add_like by entering: ")
        print("userId = '',vacationId= '60'")
        with self.like as like:
            add_like = like.add_like(userId = '',vacationId= '60')#two parameters that are in the data base
            print(add_like)

    def test_empty_value_in_vacationId_in_add_like(self):
        print ("test_add_like by entering: ")
        print("userId = '4',vacationId= ''")
        with self.like as like:
            add_like = like.add_like(userId = '4',vacationId= '')#two parameters that are in the data base
            print(add_like) 

    def test_letters_in_UserId_in_add_like (self):#str when an int type value is demanded
        print ("test_letters_in_UserId_in_add_like by entering: ")
        print("userId = 'abc',vacationId= '60'")
        with self.like as like:
            add_like = like.add_like(userId = 'abc',vacationId= '60')
            print(add_like)

    def test_letters_in_vacationId_add_like (self):#str when an int type value is demanded
        print ("test_letters_in_vacationId_add_like by entering: ")
        print("userId = '4',vacationId= 'abc'")
        with self.like as like:
            add_like = like.add_like(userId = '4',vacationId= 'abc')
            print(add_like)

    def test_wrong_userId_add_like (self):#typing a parameter that does not exist in DB
        print ("test_wrong_userId_add_like by entering: ")
        print("userId = '123',vacationId= '60'")
        with self.like as like:
            add_like = like.add_like(userId = '123',vacationId= '60')#userId not in data base
            print(add_like)

    def test_Wrong_vacationId_add_like (self):#typing a parameter that does not exist in DB
        print ("test_Wrong_vacationId_add_like by entering: ")
        print("userId = '4',vacationId= '123'")
        with self.like as like:
            add_like = like.add_like(userId = '4',vacationId= '123')#vactionId not in data base
            print(add_like)

     
    def all_tests_for_add_like (self):
        self.test_add_like()
        self.test_empty_value_in_userId_in_add_like()
        self.test_empty_value_in_vacationId_in_add_like()
        self.test_letters_in_UserId_in_add_like()
        self.test_letters_in_vacationId_add_like()
        self.test_wrong_userId_add_like()
        self.test_Wrong_vacationId_add_like()
    

    def test_delete_like(self):
        print ("test_delete_like by entering: ")
        print("userId = '4',vacationId= '60'")
        with self.like as like:
            delete_like = like.delete_like(userId = '4',vacationId= '60')#two parameters that are in the data base and in like table
            print(delete_like)


    def test_wrong_userId_delete_like(self):#typing a parameter that does not exist in DB
        print ("test_wrong_userId_delete_like by entering: ")
        print("userId = '123',vacationId= '59'")
        with self.like as like:
            delete_like = like.delete_like(userId = '123',vacationId= '59')#userId not in table
            print(delete_like)
    def test_wrong_vacationId_delete_like(self):#typing a parameter that does not exist in DB
        print ("test_wrong_userId_delete_like by entering: ")
        print("userId = '26',vacationId= '34'")
        with self.like as like:
            delete_like = like.delete_like(userId = '26',vacationId= '34')#vacationId not in table
            print(delete_like)
    def test_str_userId_delete_like(self):#wrong class type of character
        print ("test_str_userId_delete_like by entering: ")
        print("userId = 'abc',vacationId= '59'")
        with self.like as like:
            delete_like = like.delete_like(userId = 'abc',vacationId= '59')
            print(delete_like)
    def test_str_vacationId_like_delete_like(self):#wrong class type character
        print ("test_str_vacationId_like_delete_like by entering: ")
        print("userId = '26',vacationId= 'abc'")
        with self.like as like:
            delete_like = like.delete_like(userId = '4',vacationId= 'abc')
            print(delete_like)
    def test_userId_not_in_likes_table_in_delete_like(self):
        print ("test_userId_not_in_likes_table_in_delete_like by entering: ")
        print("userId = '28',vacationId= '69'")
        with self.like as like:
            delete_like = like.delete_like(userId = '28',vacationId= '69')#userId exists but not in likes table unlike vacationId that does
            print(delete_like)
    def test_vacationId_not_in_likes_table_in_delete_like(self):
        print ("test_vacationId_not_in_likes_table_in_delete_like by entering: ")
        print("userId = '26',vacationId= '66'")
        with self.like as like:
            delete_like = like.delete_like(userId = '26',vacationId= '66')#vacationId exists but not in likes table unlike userId that does
            print(delete_like)
    def test_empty_value_in_userId_in_delete_like(self):
        print ("test_empty_value_in_userId_in_delete_like by entering: ")
        print("userId = '',vacationId= '69'")
        with self.like as like:
            delete_like = like.delete_like(userId = '',vacationId= '69')
            print(delete_like)
    def test_empty_value_in_vacationId_in_delete_like(self):
        print ("test_str_vacationId_like_delete_like by entering: ")
        print("userId = '26',vacationId= ''")
        with self.like as like:
            delete_like = like.delete_like(userId = '26',vacationId= '')
            print(delete_like)

    def all_tests_for_delete_like(self):
        self.test_delete_like()
        self.test_wrong_userId_delete_like()
        self.test_wrong_vacationId_delete_like()
        self.test_wrong_vacationId_delete_like()
        self.test_str_userId_delete_like()
        self.test_str_vacationId_like_delete_like()
        self.test_userId_not_in_likes_table_in_delete_like()
        self.test_vacationId_not_in_likes_table_in_delete_like()
        self.test_empty_value_in_userId_in_delete_like()
        self.test_empty_value_in_vacationId_in_delete_like()

    def turn_on_all_tests(self):        
        self.all_tests_for_add_like()
        self.all_tests_for_delete_like()
        self.all_tests_for_register_to_system()
        self.all_tests_for_sign_in_for_registered_users()
        self.all_tests_for_vacation_functions()

        explain why self.vacation doesnt work