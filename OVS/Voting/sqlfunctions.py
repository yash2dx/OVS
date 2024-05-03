import requests
import json

def VoterInfo(voterid,password):
    import mysql.connector

    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlpassword@1234")
    query="use project"
    cursor=mydb.cursor()
    cursor.execute(query)
    query="select * from voting_voter where voterid='"+voterid+"' AND passwd='"+password+"' "
    cursor=mydb.cursor()
    cursor.execute(query)
    data=cursor.fetchall()
    id,firstname,middlename,lastname,voterid,password,email,state,statecode,phone,seatname=data[0]
    
    dictionary={'id':id,'firstname':firstname,'middlename':middlename,'lastname':lastname,'voterid':voterid,'email':email,'state':state,'statecode':statecode,'phone':phone,'seatname':seatname}
    return dictionary

#print(VoterInfo("VOT130799",'test1234'))

def VoterInfoUsingVoterid(voterid):
    import mysql.connector

    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlpassword@1234")
    query="use project"
    cursor=mydb.cursor()
    cursor.execute(query)
    query="select * from voting_voter where voterid='"+voterid+"' "
    cursor=mydb.cursor()
    cursor.execute(query)
    data=""
    id,firstname,middlename,lastname,voterid,password,email,state,statecode,phone,seatname=data[0]
    dictionary={'id':id,'firstname':firstname,'middlename':middlename,'lastname':lastname,'voterid':voterid,'email':email,'state':state,'statecode':statecode,'phone':phone,'seatname':seatname}
    return dictionary

def VoterInfoUsingID(id):
    import mysql.connector

    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlpassword@1234")
    query="use project"
    cursor=mydb.cursor()
    cursor.execute(query)
    query="select * from voting_voter where id='"+str(id)+"'"
    cursor=mydb.cursor()
    cursor.execute(query)
    data=cursor.fetchall()
    if len(data)==0:
        return ""
    else:
        id,firstname,middlename,lastname,voterid,password,email,state,statecode,seatcode,phone=data[0]
        dictionary={'id':id,'firstname':firstname,'middlename':middlename,'lastname':lastname,'voterid':voterid,'email':email,'state':state,'statecode':statecode,'seatcode':seatcode,'phone':phone}
        return dictionary

def CandidateInfo(username,password):
    import mysql.connector

    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlpassword@1234")
    query="use project"
    cursor=mydb.cursor()
    cursor.execute(query)
    query="select * from voting_candidate where username='"+username+"' AND password='"+password+"' "
    cursor=mydb.cursor()
    cursor.execute(query)
    data=cursor.fetchall()
    id,profile_pic,firstname,middlename,lastname,age,address,phone,aadhar,username,password,email,state,statecode,seatcode,partyname,symbol,vote,gender,seatname=data[0]
    dictionary={'id':id,'profile_img':profile_pic,'firstname':firstname,'middlename':middlename,'lastname':lastname,'age':age,'address':address,'phone':phone,'aadhar':aadhar,'username':username,'email':email,'state':state,'statecode':statecode,'seatcode':seatcode,'partyname':partyname,'symbol':symbol,'vote':vote,'gender':gender,'seatname':seatname}
    return dictionary

#print(CandidateInfo('VOT090499','test1234'))

def CandidateInfoUsingID(id):
    import mysql.connector

    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlpassword@1234")
    query="use project"
    cursor=mydb.cursor()
    cursor.execute(query)
    query="select * from voting_candidate where id='"+str(id)+"'"
    cursor=mydb.cursor()
    cursor.execute(query)
    data=cursor.fetchall()
    if len(data)==0:
        return ""
    else:
        id,profile_pic,firstname,middlename,lastname,age,address,phone,aadhar,username,password,email,state,statecode,seatcode,partyname,symbol,vote,gender,seatname=data[0]
        dictionary={'id':id,'profile_img':profile_pic,'firstname':firstname,'middlename':middlename,'lastname':lastname,'age':age,'address':address,'phone':phone,'aadhar':aadhar,'username':username,'email':email,'state':state,'statecode':statecode,'seatcode':seatcode,'partyname':partyname,'symbol':symbol,'vote':vote,'gender':gender,'seatname':seatname}
        return dictionary

def CandidateNameUsingID(id):
    import mysql.connector

    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlpassword@1234")
    query="use project"
    cursor=mydb.cursor()
    cursor.execute(query)
    query="select first_name,username from voting_candidate where id='"+str(id)+"'"
    cursor=mydb.cursor()
    cursor.execute(query)
    data=""
    return data[0]

def selectStateNomination():
    import mysql.connector

    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlpassword@1234")
    query="use project"
    cursor=mydb.cursor()
    cursor.execute(query)
    #query=""
    query="select distinct(voting_mainelection.State) from voting_addelections,voting_mainelection where voting_mainelection.Status=0 AND voting_addelections.MainElection_id=voting_mainelection.id"
    cursor=mydb.cursor()
    cursor.execute(query)
    data=cursor.fetchall()
    if(len(data)==0):
        return "empty"
    else:
        lst=[]
        for d in data:
            lst.append(d[0])
        return lst
    
def selectSeatNomination():
    import mysql.connector

    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlpassword@1234")
    query="use project"
    cursor=mydb.cursor()
    cursor.execute(query)
   # query=""
    query="select distinct(voting_addelections.Seats) from voting_addelections,voting_mainelection where voting_mainelection.Status=0 AND voting_addelections.MainElection_id=voting_mainelection.id"
    cursor=mydb.cursor()
    cursor.execute(query)
    data=cursor.fetchall()
    if(len(data)==0):
        return "empty"
    else:
        lst=[]
        for d in data:
            lst.append(d[0])
        return lst

def CandidateList(username):
    import mysql.connector

    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlpassword@1234")
    query="use project"
    cursor=mydb.cursor()
    cursor.execute(query)
    query="select voting_election.Candidate_Name,voting_election.Candidate_Username from voting_election,voting_mainelection,voting_voter where (voting_election.MainElection_id=voting_mainelection.id AND voting_mainElection.Status=0 ) AND (voting_election.Seat=voting_voter.seatname AND voting_voter.voterid='"+username+"');"
  
    cursor=mydb.cursor()
    cursor.execute(query)
    data=cursor.fetchall()
    if(len(data)==0):
        return ""
    else:
        dictionary=[]
        for d in data:
            dictionary.append([d[0],d[1]])
        return dictionary

def GetId(username):
    import mysql.connector

    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlpassword@1234")
    query="use project"
    cursor=mydb.cursor()
    cursor.execute(query)
    query="select voting_mainElection.id from voting_mainelection,voting_voter,voting_election where (voting_voter.voterid='"+username+"' AND voting_election.Seat=voting_voter.seatname) AND (voting_mainelection.Status=0 AND voting_election.MainElection_id=voting_mainelection.id)"
    cursor=mydb.cursor()
    cursor.execute(query)
    data=cursor.fetchall()
    if(len(data)==0):
        return ""
    else:
        data=data[0][0]
        return data
#print(GetId('VOT130799'))



def SubmitVote(username):
    print(username)
    import mysql.connector
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlpassword@1234")
    query="use project"
    cursor=mydb.cursor()
    cursor.execute(query)
    query="UPDATE voting_election SET NoofVotes=NoofVotes+1 where Candidate_Username='"+username+"'"
    print(query)
    cursor=mydb.cursor()
    cursor.execute(query)
    mydb.commit()
    query="select voting_election.MainElection_id from voting_election,voting_mainelection where (Candidate_Username='"+username+"' AND voting_mainelection.STATUS=0) AND voting_mainelection.id=voting_election.MainElection_id;"

    print(query)
    cursor=mydb.cursor()
    cursor.execute(query)
    data=cursor.fetchall()
    if len(data)==0:

        return ""
    else:
        data=data[0][0]
        return data

def checkAlreadyVoted(username,eid):
    import mysql.connector
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlpassword@1234")
    query="use project"
    cursor=mydb.cursor()
    cursor.execute(query)
    query="select EXISTS(select * from voting_alreadyvoted where Election_id='"+str(eid)+"' AND Username='"+username+"')"
    
    cursor=mydb.cursor()
    cursor.execute(query)
    data=cursor.fetchall()
    data=data[0][0]
    return data

#print(checkAlreadyVoted('VOT130799',2))


def showResultsSeatWise(state):
    import mysql.connector
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlpassword@1234")
    query="use project"
    cursor=mydb.cursor()
    cursor.execute(query)    
    query="select voting_election.Candidate_Name,voting_election.Seat from voting_election,voting_mainelection where ((NoofVotes,Seat) in (select max(NoofVotes) as votes,Seat from voting_election group by voting_election.Seat)) AND ((voting_mainelection.Status=1 AND voting_mainelection.State='"+state+"') AND (voting_mainelection.id=voting_election.MainElection_id))"
    #select Candidate_Name,Seat from voting_election,voting_addelections where ((NoofVotes,Seat) in (select max(NoofVotes) as votes,Seat from voting_election group by Seat)) AND ((voting_addelections.Status=1 AND voting_addelections.State='"+state+"') AND voting_addelections.Election_id=voting_election.Election_id)"

    cursor=mydb.cursor()
    cursor.execute(query)
    data=cursor.fetchall()
    if(len(data)==0):
        return ""
    else:
        dictionary=[]
        for d in data:
            dictionary.append([d[0],d[1]])
        return dictionary

print(showResultsSeatWise('Delhi'))

def showTimes():
    import mysql.connector
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlpassword@1234")
    query="use project"
    cursor=mydb.cursor()
    cursor.execute(query)
    query="select distinct(Start_time) from voting_addelections"
    cursor=mydb.cursor()
    cursor.execute(query)
    data=""
    return data



def showStates():
    import mysql.connector
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlpassword@1234")
    query="use project"
    cursor=mydb.cursor()
    cursor.execute(query)
    query="select State from voting_mainelection where Status=1"
    cursor=mydb.cursor()
    cursor.execute(query)
    data=cursor.fetchall()
    if(len(data)==0):
        return ""
    else:
        lst=[]
        for d in data:
            lst.append(d[0])
        return lst

print(showStates())

#print(checkAlreadyVoted('VOTSCGS01',4))
    
#print(GetId('VOTSCGS01'))

def showStatesHistory():
    import mysql.connector
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlpassword@1234")
    query="use project"
    cursor=mydb.cursor()
    cursor.execute(query)
    query="select distinct(State) from voting_mainelection where Status=1 OR Status=2"
    cursor=mydb.cursor()
    cursor.execute(query)
    data=cursor.fetchall()
    if(len(data)==0):
        return ""
    else:
        lst=[]
        for d in data:
            lst.append(d[0])
        return lst

def showElectionNames(state):
    import mysql.connector
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlpassword@1234")
    query="use project"
    cursor=mydb.cursor()
    cursor.execute(query)
    query="select distinct(Election_Name) from voting_mainelection where (Status=1 OR Status=2) AND State='"+state+"'"
    cursor=mydb.cursor()
    cursor.execute(query)
    data=cursor.fetchall()
    if(len(data)==0):
        return ""
    else:
        lst=[]
        for d in data:
            lst.append(d[0])
        return lst

def showHistory(state,election_name):
    import mysql.connector
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlpassword@1234")
    query="use project"
    cursor=mydb.cursor()
    cursor.execute(query)
    query="select ve.Election_Name,Candidate_Name,Seat,Year from voting_election ve,voting_mainelection vme where ((NoofVotes,Seat,Year) in (select max(NoofVotes) as votes,Seat,Year from voting_election group by Seat,Election_Name)) AND  ((((vme.Status=1 OR vme.Status=2)  AND vme.State='"+state+"') AND ve.Election_Name='"+election_name+"') AND (vme.id=ve.MainElection_id));"
    cursor=mydb.cursor()
    cursor.execute(query)
    data=cursor.fetchall()
    if len(data)==0:
        return ""
    else:
        lst=[]
        for d in data:
            lst.append([d[0],d[1],d[2],d[3]])
        return lst




    