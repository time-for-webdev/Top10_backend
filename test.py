import requests
import json

def change_requird_data(data):
    vpn = []
    rating = []
    remark =[]
    ct =-1
    flag = True
    for i in data :
        ct+=1
        if ct>30 :
            break
        if ct<=10 :
            if ct :
                vpn.append(i)
        else:
            if ct == 11 :
                continue
            if flag :
                rating.append(i)
                flag = False
            else :
                remark.append(i)
                flag = True
    for i in range(0,10):
        if data[vpn[i]] :
            data[vpn[i]]['rating']=data[rating[i]]
    return data        
    





URL = "http://127.0.0.1:8000/api/service/Overall%20Best%20Vpn%20of%202023/"

r = requests.get(url=URL)
data = r.json()

print(data)


vpn = []
rating = []
remark =[]
ct =-1
flag = True
for i in data :
    ct+=1
    if ct>35 :
        break
    if ct<=14 :
        if ct :
            vpn.append(i)
    else:
        if ct == 15 :
            continue
        if flag :
            rating.append(i)
            flag = False
        else :
            remark.append(i)
            flag = True


for i in range(0,10):
    print(remark[i])
    print(data[remark[i]])

for i in range(0,10):
    print(rating[i])
    print(data[rating[i]])    

    