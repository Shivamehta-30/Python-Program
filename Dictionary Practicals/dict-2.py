price={"banana": 4,"apple": 2,"orange": 1,"pear": 3}
stock=[]
tol=0
for key,value in price.items():
    print(key)
    print("price:",value)
    b=stock.append(int(input("how many do you want?")))
    print("in cart",stock)
a=list(price.values())
for i,j in zip (a,stock):
        tol=i*j
        tol+=tol
print("sum:",tol)