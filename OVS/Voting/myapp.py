import requests
import json

URL="http://127.0.0.1:8000/InputSeatEntry/"
data={'SeatName':'Dilshad Garden','State':'Delhi','Current_MLA':'Raghav Jain','Current_MP':'Sudhanshu Mishra'}
json_data=json.dumps(data)
r=requests.post(url=URL,data=json_data)
data=r.json()
print(data)