# api meraki question.deta ko manga ke json file me store kare 

import requests,json
from pprint import pprint
# x = requests.get('http://saral.navgurukul.org/api/courses')
# with open("api.json","w") as d:
#     json.dump(x.json(),d,indent=4)


# how to get slug ........api...meraki Question

x = requests.get('http://saral.navgurukul.org/api/courses').json()
with open("api.json","w") as d:
    json.dump(x,d,indent=4)
with open("api.json","r") as d1:
    p=json.load(d1)
    pprint(p)
    for i in p:
        for k in p[i]:
            print(k["id"],k["name"])
    n=int(input("enter the id:"))
    y=requests.get("http://saral.navgurukul.org/api/courses/"+str(n)+"/exercises").json()
    print(y)
    with open("raja.json","w") as f:
        json.dump(y,f,indent=4)
    a=0
    b=[]
    for i in y['data']:
        print(a," ",i["slug"])
        a+=1
        b.append(i["slug"])
    m=int(input("enter the slug number:"))
    final_data=requests.get("http://saral.navgurukul.org/api/courses/"+str(n)+"/exercise/getBySlug?slug="+str(b[m])).json()
    pprint(final_data)




# r=requests.get("http://saral.navgurukul.org/api/courses")
# with open("jaal.json","w") as f:
#     json.dump(r.json(),f,indent=4)
# with open("jaal.json","r")as f1:
#     d=json.load(f1)
#     pprint(d)
#     for i in d:
#         for j in d[i]:
#             print(j["id"],j["name"])
#     n=int(input("enter the id: "))
#     s=requests.get("http://saral.navgurukul.org/api/courses/"+str(n)+"/exercises").json()
#     print(s)
#     with open("kaal.json","w") as f2:
#         json.dump(s,f2,indent=4)
#     a=0
#     b=[]
#     for i in s['data']:
#         print(a,"",i["slug"])
#         a+=1
#         b.append(i["slug"])

    
#     m=int(input("enter the slug number: "))
#     final_data=requests.get("http://saral.navgurukul.org/api/courses/"+str(n)+"/exercise/getBySlug?slug="+str(b[m])).json()
#     pprint(final_data)

    





    




# p={}
# with open("api.json","r") as l:
#     j=json.load(l)
#     c=0
#     for i in j:
#         for k in j[i]:
#             c+=1
#             p.update({c:k["id"]})
# print(p)
# n=int(input("enter the id"))


