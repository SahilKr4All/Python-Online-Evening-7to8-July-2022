import pandas as pd
data  = [{"id":1,"Name":"Sahil","phy":99,"chem":80,"maths":98},
         {"id":2,"Name":"Ravi" ,"phy":20,"chem":70,"maths":81},
         {"id":3,"Name":"Suresh","phy":50,"chem":40,"maths":90},
         {"id":4,"Name":"Niket","phy":0,"chem":10,"maths":18},
         {"id":5,"Name":"Deepanshu","phy":10,"chem":20,"maths":80}]

  

for d in data:
    average=(d["phy"]+d["chem"]+d["maths"])//3
    d["average"]=average
    grade=None
    if average>90:
        grade="A+"
    elif average>80:
        grade="A"
    elif average>70:
        grade="B+"
    elif average>60:
        grade="B"
    elif average>50:
        grade="C"
    elif average>33:
        grade="D"
    else:
        grade="F"
    d["grade"]=grade

'''
for d in data:
    print(d["id"],d["Name"],d["average"],d["grade"])
'''

df=pd.DataFrame(data)
print(df) 
