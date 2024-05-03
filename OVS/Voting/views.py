from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.models import User
from Voting.models import AddElections, AlreadyVoted, SeatDetails, Voter,Candidate,Election
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from Voting.serializers import SeatDetailsSerializer
from Voting.sqlfunctions import *
from django.http import JsonResponse
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser 
import random
import json
import requests
import io
from django.views.decorators.csrf import csrf_exempt
# import twilio
# from twilio.rest import Client
# def mobile_verify(phone,otp):
#     account_sid ='ACfa30dd2bc2ce012b619152faa7e08a21'
#     auth_token = '9b798bc246e46b6cfdaca25a6045d312'
#     client = Client(account_sid, auth_token)

#     message = client.messages \
#         .create(
#              body='Use verification code '+otp+' to verify and login to your account',
#              from_='+15592060541',
#              status_callback='http://postb.in/1234abcd',
#              to='+91'+str(phone)
#          )

#     print(message.sid)


def generate_OTP():
    otp=str(random.randint(100000,999999))
    return otp

def otp_check(otp,sent_otp):
    if(otp==sent_otp):
        return True
    else:
        return False

# Create your views here.



def index(request):
    return render(request,"home.html")
def register_voter(request):
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        middle_name=request.POST.get('middle_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        state=request.POST.get('statename')
     
        seatcode=request.POST.get('seatcode')
        
        voter=Voter(firstname=first_name,middlename=middle_name,lastname=last_name,voterid=username,passwd=password,email=email,state=state,seatname=seatcode,phone=phone)
        voter.save()
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
    return render(request,"register_voter.html")



def login_voter(request):
   
   if request.method=="POST":
            voterid=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(username=voterid,password=password)
            print(user)
            if user is not None:
                login(request,user)
                #url='otp_verify/'+voterid
               # return redirect(url)
                
                eid=GetId(voterid)
                print(eid)
                vot=VoterInfo(voterid,password)
                context={'vot':vot,'status':checkAlreadyVoted(voterid,eid)}
                return render(request,"voters_logged_in.html",context)
                
            else:
                messages.info(request,"invalid credentials")
                return redirect("login_voter")     
            
           # return render(request,"home.html")
   else:                  
        return render(request,'login_voter.html')

#def voters_logged_in(request,username):
    #eid=GetId(username)
    #vot=VoterInfoUsingVoterid(username)
   # return render(request,"voters_logged_in.html",{'vot':vot,'status':checkAlreadyVoted(username,eid)})

def voter_profile(request,id):
    context={'vot':VoterInfoUsingID(id)}
    return render(request,"profile.html",context)

def login_candidate(request):
    if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(username=username,password=password)
            print(user)
            if user is not None:
                login(request,user)
                context={'vot':CandidateInfo(username,password)}
                
                    
                return render(request,"candidate_logged_in.html",context)
            else:
                messages.info(request,"invalid credentials")
                return redirect("login_candidate")     
            
           # return render(request,"home.html")
    else:                  
        return render(request,'login_candidate.html')
    

def register_candidate(request):
    if request.method =="POST":
         candidate=Candidate()
         candidate.profile_img=request.POST['img']
         candidate.first_name=request.POST['first_name']
         candidate.middle_name=request.POST['middle_name']
         candidate.last_name=request.POST['last_name']
         candidate.age=request.POST['age']
         candidate.address=request.POST['address']
         candidate.phone_num=request.POST['phone']
         candidate.Aadhar_card=request.POST['aadhar_no']
         candidate.username=request.POST['username']
         candidate.password=request.POST['password']
         confirm_password=request.POST['confirm_password']
         if candidate.password==confirm_password :
             candidate.email=request.POST['email']
             candidate.state=request.POST['state']
           #  candidate.statecode=request.POST['state_code']
             #candidate.seatcode=request.POST['seat_code']
             candidate.partyname=request.POST['party']
             candidate.symbol=request.POST['symbol']
             candidate.vote_receive=0
             candidate.gender=request.POST['gender']
             candidate.save()
             user = User.objects.create_user(username=candidate.username, email=candidate.email, password=candidate.password)
             user.save()
             return render(request,'home.html')

    else:       
           return render(request,'register_candidate.html')

def candidate_profile(request,id):
    context={'vot':CandidateInfoUsingID(id)}
    return render(request,"candidate_profile.html",context)

def candidate_nomination(request):
    context={
        'state':selectStateNomination,
        'seat':selectSeatNomination
    }

    if request.method=="POST":
        name=request.POST.get('name')
        mid=request.POST.get('mid')
        c_id=request.POST.get('c_id')
        username=request.POST.get('username')
        ename=request.POST.get('ename')
        eid=request.POST.get('eid')
        state=request.POST.get('state')
        seat=request.POST.get('seat')
        print(seat)
        election=Election(MainElection_id=mid,Election_id=eid,Candidate_Name=name,Candidate_Id=c_id,Election_Name=ename,Candidate_Username=username,State=state,Seat=seat)
        election.save()
        messages.info(request,"Your Nomination has been successful")
        return redirect('login_candidate')
    return render(request,"candidate_nomination.html",context)

def castVote(request):
   if request.method=="POST":
        username=request.POST.get('op')
        print(username)
        e_id=SubmitVote(username)
        username=request.user.username
        voted=AlreadyVoted(Election_id=e_id,Username=username)
        voted.save()
        
        return redirect('login_voter')
        
   username=request.user.username
   candidate_dict=CandidateList(username)
    #lst_name=candidate_dict['name']
    #lst_user=candidate_dict['user']
   print(candidate_dict)
   context={'candidate':candidate_dict}
   return render(request,'Voting.html',context)

def result(request):
    context={'states':showStates}
    if context['states']=="":
        return HttpResponse("No States Result to show")
    else:
        return render(request,'Result.html',context)
    
def resultstate(request,state):
    context={'result':showResultsSeatWise(state)}
    if(context['result']==""):
        return HttpResponse("No Results to show")
    else:
        return render(request,'ResultState.html',context)

def history(request):
    context={'states':showStatesHistory}
    
    return render(request,'History.html',context)

def historystate(request,state):
    context={'name':showElectionNames(state),'state':state}
    print(context['name'])
    return render(request,'HistoryState.html',context)

def historyelection(request,state,election_name):
    context={'record':showHistory(state,election_name)}
    return render(request,'HistoryElection.html',context)

#def otp_verification(request,voterid):
    #    eid=GetId(voterid)
    #    vot=VoterInfoUsingVoterid(voterid)
    #    phone=vot['phone']
    #    print(phone)
    #    otp=generate_OTP()
    #    mobile_verify(phone,otp)
    #    if request.method=="POST":
    #        sent_otp=request.POST.get('otp')
    #        otp_status=otp_check(otp,sent_otp)
    #        if otp_status:
    #            
    #        else:
    #            
    #            return render(request,'otp_verify.html',{'status':1})
    #    else:
    #        context={'id':voterid,'status':0}
    #        return render(request,'otp_verify.html',context) 

@api_view(['GET'])
def apiOverview(request):
    data={
        'name':'Sudhanshu',
         'roll no.':'49',
         'Phone':'9953323859'
    }
    return Response(data)

def output_SeatEntry(request):
    seat=SeatDetails(SeatName='NandNagri' , State='Delhi',Current_MLA='Aditya',Current_MP='Mahesh Chand')
    seat.save()

    # Converting into serializing object

    SeatSerializer=SeatDetailsSerializer(seat)
    print(SeatSerializer.data)
    # json_data=JSONRenderer().render(SeatSerializer.data)
    # print(type(json_data))
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(SeatSerializer.data)

@csrf_exempt
def CreateSeatEntry(request):
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=SeatDetailsSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
    return HttpResponse("Here I am !!!!")