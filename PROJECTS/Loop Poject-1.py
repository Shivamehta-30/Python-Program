answer = 0
user="yes"
while user=="yes":
   a = int(input("Enter any value"))
   b = int(input("Enter any value "))

   while b > 0:
      print("A=",a,"B=",b)
      if (b%2 != 0):
         print("B is odd so adding A",a)
         answer=answer+a
         a=a*2
         b=int(b/2)
      else:
         a=a*2
         b=int(b/2)
   print("the product is", (answer))
   user=input("do you want to continue (yes/no)?:")

