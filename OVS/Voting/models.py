from django.db import models
from Voting.sqlfunctions import *
# Create your models here.
class Voter(models.Model):
    firstname = models.CharField(max_length=100)
    middlename=models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    voterid=models.CharField(max_length=20,unique=True)
    passwd=models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    state=models.CharField(max_length=30)
    statecode=models.IntegerField(default=0)
    seatname=models.CharField(max_length=30,default="")
    phone=models.BigIntegerField()

    def __str__(self):
        return self.firstname+" "+self.middlename+" "+self.lastname

class Candidate(models.Model):
     profile_img =  models.ImageField(upload_to='pics/')
     first_name  =  models.CharField(max_length=100)
     
     middle_name =  models.CharField(max_length=100)
     last_name   =  models.CharField(max_length=100)

     age         =  models.IntegerField()
     address     =  models.CharField(max_length=100)
     phone_num=models.CharField(max_length=10)
     Aadhar_card =  models.CharField(max_length=100)
     username    =  models.CharField(max_length=20,unique=True)
     password    =  models.CharField(max_length=40)
     email       =  models.CharField(max_length=100)
     state       =  models.CharField(max_length=100)
     statecode   =  models.IntegerField(default=0)
     seatcode    =  models.IntegerField(default=0)
     seatname=models.CharField(max_length=30,default="")
     partyname   =  models.CharField(max_length=20)
     partyname   =  models.CharField(max_length=20)
     symbol      =  models.CharField(max_length=20)
     vote_receive=  models.IntegerField()
     gender      =  models.CharField(max_length=20)

class AddElections(models.Model):
    Election_id=models.BigAutoField(primary_key=True)
    Election_name=models.CharField(max_length=50)
    Year=models.CharField(max_length=10)
    
    State=models.CharField(max_length=30)
    Seats=models.CharField(max_length=30)
    MainElection_id=models.BigIntegerField(default=0)

    def __str__(self):
        return self.Election_name+" "+self.Seats+" ("+"Id= "+str(self.MainElection_id)+ " )"





class Election(models.Model):
    MainElection_id=models.BigIntegerField(default=0)
    Election_id=models.BigIntegerField()
    Candidate_Name=models.CharField(max_length=30,default="")
    Candidate_Id=models.BigIntegerField()
    Election_Name=models.CharField(max_length=50)
    Candidate_Username=models.CharField(max_length=20)
#    Candidate_Id=models.ForeignKey(Candidate,on_delete=models.CASCADE)
  #  PartyName=models.CharField(max_length=20)
    State=models.CharField(max_length=30)
    Seat=models.CharField(max_length=30)
    NoofVotes=models.PositiveBigIntegerField(default=0)
    

class AlreadyVoted(models.Model):
    Election_id=models.BigIntegerField()
    Username=models.CharField(max_length=20)

class MainElection(models.Model):
    
    Election_Name=models.CharField(max_length=50)
    State=models.CharField(max_length=30)
    Status=models.IntegerField(default=0)
    Year=models.CharField(max_length=10)
    Start_date=models.DateField()
    End_date=models.DateField()
    Start_time=models.TimeField()
    End_time=models.TimeField()
    
    def __str__(self):
        return self.Election_Name+" ("+"Id= "+str(self.id)+ " )"

class SeatDetails(models.Model):
    SeatName = models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    Current_MLA=models.CharField(max_length=50)
    Current_MP = models.CharField(max_length=50)
