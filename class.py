import datetime
class User:
    '''A member of FriendFace. For now we are only storing their name and birthday. But soon we will store uncomfortable amount of user information'''
    public_attr = 'public'
    def __init__(self):
        self.full_name= 'full_name'
        self.birthday= 'birthday' #yyyymmdd
        self.phone = '123456'
    # def __init__(self, full_name, birthday):
    #     self.full_name= full_name
    #     self.birthday= birthday #yyyymmdd
    #     self.phone = '123456'

    def age(self):
        '''Calculate and return the age'''
        today = datetime.date(2020,8,14) 
        yyyy= int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy,mm,dd)
        age_in_days= (today-dob).days
        age_in_years= age_in_days/365
        return int(age_in_years)

# user1=User('Linn Kern','19941120')
user1 = User()
print(user1.age())