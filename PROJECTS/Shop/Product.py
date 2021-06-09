class Product:
    id=0
    name=""
    qty=0
    rate=0.0
    price=0.0


    def setProduct(self):
        self.id=int(input("Enter Product Id:"))
        self.name=input("Enter Product Name :")
        self.qty=int(input("Enter Product Qty :"))
        self.rate=float(input("Enter Product Rate:"))
        self.price=self.qty*self.rate

    def getProduct(self):
        print(str(self.id).ljust(10,' '),
              self.name.ljust(20,' '),
              str(self.qty).ljust(10,' '),
              str(self.rate).ljust(10,' '),
              str(self.price).ljust(10,' '))

