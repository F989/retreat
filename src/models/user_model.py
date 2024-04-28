class UserModel:

    def __init__(self,userId,fname,lname,Email,Password,roleId):
        self.userId = userId
        self.fname = fname
        self.lname = lname
        self.Email = Email
        self.Password = Password
        self.roleId = roleId

    def __str__(self):
        return (f"userId: {self.userId},fname: {self.fname},lname: {self.lname},Email: {self.Email},Password: {self.Password},roleId: {self.roleId} ")

    @staticmethod
    def dictionary_to_user(dictionary):
        if dictionary is None:#to prevent system crash when sql has no result
            return None
        userId = dictionary.get("userId")  
        fname = dictionary.get('fname')
        lname = dictionary.get('lname')
        Email = dictionary.get('Email')
        Password = dictionary.get('Password')
        roleId = dictionary.get('roleId')
        user = UserModel(userId, fname, lname, Email, Password, roleId)
        return user

 
    
    @staticmethod
    def dictionaries_to_users(list_of_dictionary):
        users = []
        for item in list_of_dictionary:
            user = UserModel.dictionary_to_user(item)
            users.append(user)
        return users

 
           
    


 
    