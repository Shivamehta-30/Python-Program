class Personal_Info:
    id=0
    name=""
    address=""
    phno=""

    def setPersonal_Info(self,title):
        self.id=int(input("Enter "+title+" Id:"))
        self.name=input("Enter "+title+" Name:")
        self.address=input("Enter "+title+" address:")
        self.phno=input("Enter "+title+" phno:")

    def getPersonal_Info(self,title):
        print(title," Id:",self.id)
        print(title," Name:",self.name)
        print(title," Address:",self.address)
        print(title," Phno:",self.phno)
