
try:
    value = 10/0                                        #at zada cislo pokud ne tak 
    number= int(input("enter a number: "))    #int vloz jen cele cislo
    print(number)
    
except ZeroDivisionError as err:        #err vypise konkretni error
    print(err)
except ValueError:
    print("enter a number Dickhead")