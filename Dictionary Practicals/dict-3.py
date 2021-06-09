name=input("enter your string")
dic={}
for i in name:
    dic[i]=dic.get(i,0)+1
print(dic)
