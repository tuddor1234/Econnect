
class User:
    def __init__(self,name,email,department,profile_pic):
        self.name=str(name)
        self.email=str(email)
        self.profile_pic=str(profile_pic) #URL FOR PICTURE
        self.trainings=[]
        self.department=str(department)
    def enroll(self,tartrain):
        if tartrain is Training:
            self.trainings.add(tartrain)
    def leave(self,tartrain):
        for tr in self.trainings:
            if tr.tname == tartrain.tname:
                self.trainings.remove(tr)
                break
    

class Trainer(User):
    def __init__(self,name,email,department,profile_pic):
        super().__init__(name, email, department, profile_pic)
        self.trainerat=[]


class Profile:
    def __init__(self,user):
        self.name=user.name
        self.email=user.email
        self.department=user.department
        self.training_list=user.trainings
        
        
class Training:
    def __init__(self,name,tra):
        self.tname=str(name)
        self.materials=[]
        tra.trainerat.append(self)
        self.trainer=tra
        
"""
bruh=Trainer("Alpha","Alpha@ree.com","marketing","URL")
bro=User("Papa","Papa@ree.com","marketing","URLL")
t1=Training("Roasting",bruh)
t2=Training("Eating",bruh)

bro.enroll(t1)
bro.enroll(t2)
bro.leave(t2)

"""
