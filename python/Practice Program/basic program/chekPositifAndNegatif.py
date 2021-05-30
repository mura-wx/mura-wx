try :
    number=int(input("Enter Number : "))

    if number < 0:
        print("The entered number is negatif")
    elif number > 0:
        print("The entered number is positif")
    if number == 0:
        print("number is Zero")

except ValueError :
    print('The input is not a number !')