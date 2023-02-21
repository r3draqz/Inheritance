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
        print(self.__name)
        print(self.__address)
        print(self.__number)

    


    #make get methods for the attributes

class Customer(Person):
    def __init__(self, name, address, number, custNum, mailList):
        
        Person.__init__(self, name, address, number)

        self.__custNum = custNum
        self.__mailList = mailList

    def get_mailList(self):
        return self.__mailList

    def getname(self):
        return self.__name

    def getaddress(self):
        return self.__address

    def print_person(self):
        # print(self.__name)
        # print(self.__address)
        # print(self.__number)
        print(self.__custNum)
        print(self.__mailList)
