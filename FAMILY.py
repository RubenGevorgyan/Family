from enum import Enum
class Role(Enum):
    Father=1
    Mother=2
    Son=3
    Daughter=4
    Relative=5
    Friend=6
class Family:
    def __init__(self, members_number):
        self.__members = [members_number]
        for i in range (0,members_number):
            self.__members[i]=Person()
    def __get_member__(self,role,name):
        for i in range (0,self.__members.count()):
            if(self.__members[i].__get_name__().lower() == name.lower() and self.__members[i].__get_role__().lower()==role.lower()):
                return self.__members[i]
    def __get_length__(self):
        return self.__members.count()
    def __get_all_members__(self):
        return self.__members
class Person:
    def __init__(self):
        self.__role=Role(int(input("Input Role: \nFather=1\nMother=2\nSon=3\nDaughter=4\nRelative=5\nFriend=6 ")))
        self.__name=input("Input name")
        self.__phone=input("Input phone number")
    def __get_role__(self):
        return self.__role.name
    def __get_name__(self):
        return self.__name
    def __get_phone__(self):
        return self.__phone
class Birthday_Party:
    def __init__(self,hobelyard_name,hobelyard_role):
        self.__hobelyard=Family.__get_member__(hobelyard_name,hobelyard_role)
        self.__members=Family.__get_all_members__()
        for i in  Family.__get_length__():
            print(i+ "  "+ self.__members[i].__get_name__()+"  "+self.__members[i].__get_role__())
        k=1
        i=0
        self.invited= []
        while(k!=-1):
            k=int(input("Select by index who is invited, if you finished input -1"))
            if k!=-1:
                self.invited=self.__members[i]
                i=i+1
    def Happy_Birthday(self):
        print ("HAPPY BIRTHDAY "+self.__hobelyard.__get_name__()+ " \n All yor friends and family members came here including")
        for i in self.invited.count():
            print(self.invited[i].__get_name__())
class main():
    Family(int(input("Input number of family members/relatives/friends")))
main()
