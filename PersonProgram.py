import PersonClass as pc

def main():
    name = 'Sue Miller'
    address = '12345 Cherry Ln'
    number = '1234567890'
    custNum = '004'
    mailList = True

    customer = pc.Customer(name, address, number, custNum, mailList)

    person = pc.Person(name, address, number)

    person.print_person()
    customer.print_person()

main()
