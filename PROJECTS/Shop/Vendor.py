from Product import Product
from Personal_Info import Personal_Info

class Vendor(Personal_Info):
    billno=0
    billdate=""
    totalamount=0
    discount=0
    gst=0
    netamount=0
    product_list=""

    def setVendor(self):
        self.billno=int(input("Enter Bill No:"))
        self.billdate=input("Enter Bill Date:")

        self.setPersonal_Info("Vendor")

        self.product_list=[]
        op="yes"
        while op.lower()=="yes":
            product=Product()
            product.setProduct()
            self.totalamount=self.totalamount+product.price
            self.product_list.append(product)
            op=input("do you want to add another product(yes/no)?:")

        self.discount=float(input("Enter Discount(%):"))
        self.discount=(self.totalamount*self.discount)/100
        self.gst = float(input("Enter GST(%):"))
        self.gst = (self.totalamount * self.gst) / 100
        self.netamount=self.totalamount+self.gst-self.discount


    def getVendor(self):
        print("Bill No:",self.billno)
        print("Bill Date:",self.billdate)

        self.getPersonal_Info("Vendor")
        print("id".ljust(10," "),
              "Name".ljust(20," "),
              "Qty".ljust(10," "),
              "Rate".ljust(10," "),
              "Price".ljust(10," "))
        for product in self.product_list:
            product.getProduct()

        print("\n Total Amount :",self.totalamount)
        print("Discount :",self.discount)
        print("GST:",self.gst)
        print("Net Amount :",self.netamount)

