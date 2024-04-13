class UserModel:

    def __init__(self,userId,fname,lname,Email,Password,roleId):
        self.userId = userId
        self.fname = fname
        self.lname = lname
        self.Email = Email
        self.Password = Password
        self.roleId = roleId

    def ___str__(self):
        return (f"userId: {self.userId},fname: {self.fname},lname: {self.lname},Email: {self.Email},Password: {self.password},roleId: {self.roleId} ")

    @staticmethod
    def dictionary_to_user(dictionary,):
        userId = dictionary["userId"]
        fname = dictionary['fname']
        lname = dictionary['lname']
        Email = dictionary['Email']
        password = dictionary['password']
        roleId = dictionary['roleId']
        user = UserModel(userId,fname,lname,Email,password,roleId)
        return user

    @staticmethod
    def dictionaries_to_users(list_of_dictionary):
        users = []
        for item in list_of_dictionary:
            user = UserModel.dictionary_to_user(item)
            users.append(user)
            return users
        
    


 
    