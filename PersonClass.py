# dont make the attributes in super class hidden or keep them hidden and print person from person superclass

class Person:
    def __init__(self, name, address, number):
        self.__name = name
        self.__address = address
        self.__number = number

    def getname(self):
        return self.__name

    def getaddress(self):
        return self.__address

    def getnumber(self):
        return self.__number

    def print_person(self):
        print('Name:', self.__name)
        print('Address:', self.__address)
        print('Phone:', self.__number)

    


    #make get methods for the attributes

class Customer(Person):
    def __init__(self, name, address, number, custNum, mailList):
        
        Person.__init__(self, name, address, number)

        self.__custNum = custNum
        self.__mailList = mailList

    def get_mailList(self):
        return self.__mailList

    def getname(self):
        return self.name

    def getaddress(self):
        return self.__address

    def print_person(self):
        Person.print_person(self) # cant just access attributes directly because they're hidden
        
        print('Customer number:', self.__custNum)
        
        if self.__mailList:
            print('You are on the mailing list')
        else:
            print('You are NOT on the mailing list')
