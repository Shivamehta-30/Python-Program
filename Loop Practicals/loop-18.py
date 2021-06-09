no=1
total=0
while no<=7:
    print(no)
    j=1
    fact=1
    while j<=no:
        fact=j*fact
        j+=1
    print("no:",no," Fact:",fact)
    total += no/fact;
    no+=1

print("total :",total)
